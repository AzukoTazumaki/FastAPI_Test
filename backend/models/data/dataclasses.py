from dataclasses import dataclass
from typing import ClassVar
from models.data.data_music.albums import albums_list
from models.data.data_music.tracks import tracks_list
from models.data.data_music.artists import artists_list
from models.data.data_music.featurings import featurings_list
from models.data.data_music.singles import singles_list
from models.data.data_music.albums_tracks import albums_tracks_list
from models.data.data_music.artists_tracks import artists_tracks_list
from models.data.data_music.albums_artists import albums_artists_list
from models.data.data_music.keys import keys_list
from models.data.data_music.products import products_list
from models.data.data_music.genres import genres_list
from models.data.data_music.lyrics import lyrics_list


@dataclass(frozen=True)
class RawDataMusic:
    albums: ClassVar[list[dict]] = albums_list
    tracks: ClassVar[list[dict]] = tracks_list
    artists: ClassVar[list[dict]] = artists_list
    featurings: ClassVar[list[dict]] = featurings_list
    singles: ClassVar[list[dict]] = singles_list
    albums_tracks: ClassVar[list[dict]] = albums_tracks_list
    artists_tracks: ClassVar[list[dict]] = artists_tracks_list
    albums_artists: ClassVar[list[dict]] = albums_artists_list
    keys: ClassVar[list[dict]] = keys_list
    products: ClassVar[list[dict]] = products_list
    genres: ClassVar[list[dict]] = genres_list
    lyrics: ClassVar[list[dict]] = lyrics_list


@dataclass(frozen=True)
class RawDataDevelopment:
    pass
