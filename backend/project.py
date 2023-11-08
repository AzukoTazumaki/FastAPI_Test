import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from models.models import DatabaseMusic
from db import Selections
from starlette.exceptions import HTTPException as StarletteHTTPException
from sqlalchemy.exc import IntegrityError


@asynccontextmanager
async def startup(app: FastAPI):
    yield
    try:
        db = DatabaseMusic()
        db.create_tables()
        db.create_projects()
        db.close_session()
    except IntegrityError:
        pass


app = FastAPI(lifespan=startup)

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=RedirectResponse)
def index():
    return '/home'


@app.get("/home", response_class=JSONResponse)
async def index():
    db = Selections()
    last_releases = db.select_last_releases()
    products_list = db.select_products(None)
    return {
        "last_releases": last_releases,
        "products": [products_list[4], products_list[3], products_list[1]]
    }


@app.get("/products", response_class=JSONResponse)
def products():
    db = Selections()
    products_list = db.select_products(None)
    return {"products": products_list}


@app.get("/products/{product_id}", response_class=JSONResponse)
def albums_playlist(product_id: int):
    db = Selections()
    product = db.select_products(product_id)
    return {"product": product}


@app.get("/projects", response_class=JSONResponse)
def projects():
    db = Selections()
    albums = db.select_albums(None)
    singles = db.select_singles()
    featurings = db.select_featurings()
    return {"albums": albums, "singles": singles, "featurings": featurings}


@app.get("/playlist/albums/{album_id}", response_class=JSONResponse)
def albums_playlist(album_id: int):
    db = Selections()
    one_album = db.select_albums(album_id)
    return {"album": one_album}


@app.get("/playlist/{project_name}", response_class=JSONResponse)
def singles_playlist(project_name: str):
    tracks = None
    playlist_title = project_name.capitalize()
    db = Selections()
    if project_name == 'singles':
        tracks = db.select_singles()
    elif project_name == 'featurings':
        tracks = db.select_featurings()
    return {"tracks": tracks, "title": playlist_title}


@app.get("/extras", response_class=JSONResponse)
def order():
    db = Selections()
    genres = db.select_genres()
    return {"genres": genres}


# @app.exception_handler(StarletteHTTPException)
# async def my_custom_exception_handler(request: Request, exception: StarletteHTTPException):
#     if exception.status_code == 404:
#         return templates.TemplateResponse('errors/404.html', {'request': request})


if __name__ == '__main__':
    uvicorn.run('project:app', host='127.0.0.1', port=8000, reload=True)
