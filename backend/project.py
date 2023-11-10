from typing import List
import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy import desc
from sqlmodel import Session, select, create_engine
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
from models.init_db import InitEnvironmentSettings
from models.models import *

app = FastAPI()
db = InitEnvironmentSettings()
db_url = db.db_url
engine = create_engine(db_url)


origins = [
    'http://localhost:3000',
    'http://localhost:3001'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_session():
    with Session(engine) as session:
        yield session


@app.get("/read_albums", response_model=List[Albums])
def read_albums(session: Session = Depends(get_session)) -> list[Albums]:
    albums = session.exec(select(Albums)).all()
    return albums


@app.get("/read_albums_tracks_artists")
def read_albums_tracks_artists(session: Session = Depends(get_session)) -> list[dict]:
    albums_data = session.exec(select(Albums)).all()
    albums_tracks_artists = [
        {
            'title': album.title,
            'description': album.description,
            'date_release': album.date_release,
            'cover': album.cover,
            'tracks': [
                {
                    'title': track.title,
                    'duration': f'{str(track.duration).split(":")[1]}:{str(track.duration).split(":")[2]}',
                    'date_release': track.date_release.strftime('%d %B %Y'),
                    'artists': [artist.name for artist in track.artists]
                } for track in album.tracks
            ],
            'artists': [artist.name for artist in album.artists]
        } for album in albums_data
    ]
    return albums_tracks_artists


@app.get("/read_albums_artists")
def read_albums_artists(session: Session = Depends(get_session)) -> list:
    albums_data = session.exec(select(Albums)).all()
    albums_artists = [
        {
            'title': album.title,
            'description': album.description,
            'date_release': album.date_release,
            'cover': album.cover,
            'artists': [artist.name for artist in album.artists]
        } for album in albums_data
    ]
    return albums_artists


@app.get("/read_albums/{album_id}", response_model=Albums)
def read_albums(*, session: Session = Depends(get_session), album_id: int):
    album = session.get(Albums, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


@app.get("/read_albums_tracks_artists/{album_id}", response_class=JSONResponse)
def read_album_tracks_artists(*, session: Session = Depends(get_session), album_id: int):
    album = session.get(Albums, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return {'album': album, 'tracks': album.tracks, 'artists': album.artists}


@app.get("/read_albums_artists/{album_id}", response_class=JSONResponse)
def read_album_artists(*, session: Session = Depends(get_session), album_id: int):
    album = session.get(Albums, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return {'album': album, 'artists': album.artists}


@app.get("/read_last_releases")
def read_album_artists(*, session: Session = Depends(get_session)) -> list[dict]:
    last_releases = []
    last_albums = session.exec(select(Albums).order_by(desc(Albums.date_release)).limit(3)).all()
    last_singles = session.exec(select(Tracks).join(Tracks.single).order_by(desc(Tracks.date_release)).limit(3)).all()
    last_featurings = session.exec(select(Tracks).join(Tracks.featuring).order_by(desc(Tracks.date_release)).limit(3)).all()
    last_releases += [
        {
            'id': release.id,
            'title': release.title,
            'artists': [artist.name for artist in release.artists],
            'sort_key': release.date_release,
            'date_release': release.date_release.strftime('%d %B %Y'),
            'is_album': True
         } for release in last_albums
    ]
    last_releases += [
        {
            'id': release.id,
            'title': release.title,
            'artists': [artist.name for artist in release.artists],
            'sort_key': release.date_release,
            'date_release': release.date_release.strftime('%d %B %Y'),
            'is_single': True
        } for release in last_singles
    ]
    last_releases += [
        {
            'id': release.id,
            'title': release.title,
            'artists': [artist.name for artist in release.artists],
            'sort_key': release.date_release,
            'date_release': release.date_release.strftime('%d %B %Y'),
            'is_featuring': True
        } for release in last_featurings
    ]
    last_releases.sort(key=lambda item: item['sort_key'], reverse=True)
    return last_releases[:3]


@app.get("/read_products", response_model=List[Products])
def read_products(session: Session = Depends(get_session)):
    all_products = session.exec(select(Products)).all()
    products = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'old_price': product.old_price,
            'description': product.description
        } for product in all_products
    ]
    return products


@app.get("/read_products/{product_id}", response_model=Products)
def read_product(*, session: Session = Depends(get_session), product_id: int):
    product = session.get(Products, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.get("/read_tracks", response_model=List[Tracks])
def read_tracks(session: Session = Depends(get_session)):
    tracks = session.exec(select(Tracks)).all()
    return tracks


@app.get("/read_tracks/{track_id}", response_class=JSONResponse)
def read_track(*, session: Session = Depends(get_session), track_id: int):
    track = session.get(Tracks, track_id)
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    return {'track': track, 'artists': track.artists}


@app.get("/read_singles")
def read_tracks(session: Session = Depends(get_session)) -> list[dict]:
    all_singles = session.exec(select(Tracks).join(Tracks.single)).all()
    singles = [
        {
            'id': single.id,
            'title': single.title,
            'duration': f'{str(single.duration).split(":")[1]}:{str(single.duration).split(":")[2]}',
            'date_release': single.date_release.strftime('%d %B %Y'),
            'artists': [artist.name for artist in single.artists]
        } for single in all_singles
    ]
    return singles


@app.get("/read_singles/{single_id}", response_class=JSONResponse)
def read_track(*, session: Session = Depends(get_session), single_id: int):
    single = session.get(Tracks, single_id)
    if not single:
        raise HTTPException(status_code=404, detail="Single not found")
    return single


@app.get("/read_featurings")
def read_featurings(session: Session = Depends(get_session)) -> list[dict]:
    all_featurings = session.exec(select(Tracks).join(Tracks.featuring)).all()
    featurings = [
        {
            'id': featuring.id,
            'title': featuring.title,
            'duration': f'{str(featuring.duration).split(":")[1]}:{str(featuring.duration).split(":")[2]}',
            'date_release': featuring.date_release.strftime('%d %B %Y'),
            'artists': [artist.name for artist in featuring.artists]
        } for featuring in all_featurings
    ]
    return featurings


@app.get("/read_featurings/{featuring_id}", response_class=JSONResponse)
def read_featuring(*, session: Session = Depends(get_session), featuring_id: int):
    featuring = session.get(Tracks, featuring_id)
    if not featuring:
        raise HTTPException(status_code=404, detail="Single not found")
    return featuring


# @app.get("/playlist/albums/{album_id}", response_class=JSONResponse)
# def albums_playlist(album_id: int):
#     db = Selections()
#     one_album = db.select_albums(album_id)
#     return {"album": one_album}
#
#
# @app.get("/playlist/{project_name}", response_class=JSONResponse)
# def singles_playlist(project_name: str):
#     tracks = None
#     playlist_title = project_name.capitalize()
#     db = Selections()
#     if project_name == 'singles':
#         tracks = db.select_singles()
#     elif project_name == 'featurings':
#         tracks = db.select_featurings()
#     return {"tracks": tracks, "title": playlist_title}


# @app.exception_handler(StarletteHTTPException)
# async def my_custom_exception_handler(request: Request, exception: StarletteHTTPException):
#     if exception.status_code == 404:
#         return templates.TemplateResponse('errors/404.html', {'request': request})


if __name__ == '__main__':
    uvicorn.run('project:app', host='127.0.0.1', port=8000, reload=True)
