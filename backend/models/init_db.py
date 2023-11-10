from datetime import time
from sqlmodel import SQLModel, create_engine, Session
from .tables.ArtistsTracks import ArtistsTracks
from .tables.AlbumsArtists import AlbumsArtists
from .tables.Artists import Artists
from .tables.Featurings import Featurings
from .tables.Albums import Albums
from .tables.Singles import Singles
from .tables.Tracks import Tracks
from .tables.AlbumsTracks import AlbumsTracks
from .tables.Products import Products
from .tables.Lyrics import Lyrics
from .tables.Genres import Genres
from .tables.Keys import Keys
from .tables.Beats import Beats
from .tables.Mixing import Mixing
from .tables.Mastering import Mastering
from .tables.MixingAndMastering import MixingAndMastering
from .tables.Ghostwriting import Ghostwriting
from .settings import Settings
from .data.dataclasses import RawDataMusic


class InitEnvironmentSettings:
    def __init__(self):
        self.settings = Settings()
        self.settings.load_dotenv_file()
        self.db_url: str = self.settings.get_db_url()
        self.engine = create_engine(self.db_url, echo=True)


class DatabaseMusic(InitEnvironmentSettings):
    def __init__(self):
        super().__init__()
        self.data_music = RawDataMusic
        self.session = Session(bind=self.engine)
        self.tables: list = [
            self.create_albums, self.create_tracks, self.create_lyrics,
            self.create_artists, self.create_singles, self.create_featurings,
            self.create_albums_tracks, self.create_albums_artists, self.create_artists_tracks,
            self.create_products, self.create_genres, self.create_keys
        ]

    def create_tables(self):
        with self.engine.connect() as connection:
            connection.execution_options(isolation_level='AUTOCOMMIT')
            SQLModel.metadata.create_all(connection)

    def create_projects(self):
        for table in self.tables:
            table()

    def create_albums(self):
        for album in self.data_music.albums:
            self.session.add(
                Albums(title=album['title'], description=album['description'],
                       cover=album['cover'], date_release=album['date_release']))
        self.session.commit()

    def create_tracks(self):
        for track in self.data_music.tracks:
            self.session.add(
                Tracks(title=track['title'], duration=time.fromisoformat(track['duration']),
                       date_release=track['date_release'], track_position_in_album=track['track_position_in_album']))
        self.session.commit()

    def create_lyrics(self):
        for text in self.data_music.lyrics:
            self.session.add(Lyrics(lyrics=text['lyrics'], track_id=text['track_id']))
        self.session.commit()

    def create_artists(self):
        for artist in self.data_music.artists:
            self.session.add(Artists(name=artist['name']))
        self.session.commit()

    def create_singles(self):
        for single in self.data_music.singles:
            self.session.add(Singles(track_id=single['track_id']))
        self.session.commit()

    def create_featurings(self):
        for featuring in self.data_music.featurings:
            self.session.add(Featurings(track_id=featuring['track_id']))
        self.session.commit()

    def create_albums_tracks(self):
        for bunch in self.data_music.albums_tracks:
            self.session.add(AlbumsTracks(album_id=bunch['album_id'], track_id=bunch['track_id']))
        self.session.commit()

    def create_albums_artists(self):
        for bunch in self.data_music.albums_artists:
            self.session.add(AlbumsArtists(album_id=bunch['album_id'], artist_id=bunch['artist_id']))
        self.session.commit()

    def create_artists_tracks(self):
        for bunch in self.data_music.artists_tracks:
            self.session.add(ArtistsTracks(artist_id=bunch['artist_id'], track_id=bunch['track_id']))
        self.session.commit()

    def create_products(self):
        for product in self.data_music.products:
            self.session.add(
                Products(name=product['name'], price=product['price'],
                         old_price=product['old_price'], description=product['description']))
        self.session.commit()

    def create_genres(self):
        for genre in self.data_music.genres:
            self.session.add(Genres(name=genre['name'], description=genre['description']))
        self.session.commit()

    def create_keys(self):
        for key in self.data_music.keys:
            self.session.add(Keys(name=key['name']))
        self.session.commit()

    def close_session(self):
        self.session.close()
