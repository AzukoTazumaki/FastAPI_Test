from models.tables.Products import Products
from models.init_db import InitEnvironmentSettings
from sqlmodel import select, desc, create_engine, Session
from models.tables.Albums import Albums
from models.tables.Tracks import Tracks
from models.tables.Genres import Genres


class Selections(InitEnvironmentSettings):
    def __init__(self):
        super().__init__()
        self.engine = create_engine(self.db_url)
        self.session = Session(bind=self.engine)
        self.albums_statement = select(Albums).group_by(Albums)
        self.singles_statement = select(Tracks).join(Tracks.single).group_by(Tracks)
        self.featurings_statement = select(Tracks).join(Tracks.featuring).group_by(Tracks)
        self.products_statement = select(Products).order_by(Products.id)
        self.genres_statement = select(Genres)
        self.albums = self.session.execute(self.albums_statement).scalars()
        self.all_singles = self.session.execute(self.singles_statement).scalars()
        self.all_featurings = self.session.execute(self.featurings_statement).scalars()
        self.all_products = self.session.execute(self.products_statement).scalars()
        self.all_genres = self.session.execute(self.genres_statement).scalars()

    def select_albums(self, album_id: int | None):
        if album_id is None:
            return self.albums.all()
        else:
            one_album_statement = self.albums_statement.where(Albums.id == album_id)
            one_album = self.session.execute(one_album_statement).scalars().one()
            return one_album

    def select_singles(self):
        result = [
            {
                'id': single.id,
                'title': single.title,
                'date_release': single.date_release.strftime('%d %B %Y'),
                'artists': single.artists,
                'duration': f'{str(single.duration).split(":")[0]}:{str(single.duration).split(":")[1]}',
                'text': single.text
            } for single in self.all_singles
        ]
        return result

    def select_featurings(self):
        result = [
            {
                'id': featuring.id,
                'title': featuring.title,
                'date_release': featuring.date_release.strftime('%d %B %Y'),
                'artists': featuring.artists,
                'duration': f'{str(featuring.duration).split(":")[0]}:{str(featuring.duration).split(":")[1]}',
                'text': featuring.text
            } for featuring in self.all_featurings
        ]
        return result

    def select_last_releases(self):
        last_releases = []
        db_last_albums_scalars = self.session \
            .execute(select(Albums).join(Albums.artists).order_by(desc(Albums.date_release)).limit(3)).scalars()
        db_last_singles_scalars = self.session \
            .execute(select(Tracks).join(Tracks.single).join(Tracks.artists).group_by(Tracks)
                     .order_by(desc(Tracks.date_release)).limit(3)).scalars()
        db_last_featurings_scalars = self.session \
            .execute(select(Tracks).join(Tracks.featuring).join(Tracks.artists).group_by(Tracks)
                     .order_by(desc(Tracks.date_release)).limit(3)).scalars()
        for release in db_last_singles_scalars:
            last_releases.append({
                'id': release.id, 'title': release.title, 'artists': release.artists,
                'date_release': release.date_release, 'is_single': True
            })
        for release in db_last_featurings_scalars:
            last_releases.append({
                'id': release.id, 'title': release.title, 'artists': release.artists,
                'date_release': release.date_release, 'is_featuring': True
            })
        for release in db_last_albums_scalars:
            last_releases.append({
                'id': release.id, 'title': release.title, 'artists': release.artists,
                'date_release': release.date_release, 'is_album': True
            })
        last_releases.sort(key=lambda item: item['date_release'], reverse=True)
        return last_releases[:3]

    @staticmethod
    def match_product_name(product_id: int):
        match product_id:
            case 1:
                return select(Products).join(Products.beats)
            case 2:
                return select(Products).join(Products.mixing)
            case 3:
                return select(Products).join(Products.mastering)
            case 4:
                return select(Products).join(Products.mixing_and_mastering)
            case 5:
                return select(Products).join(Products.ghostwriting)

    def select_products(self, product_id: int | None):
        if product_id is None:
            result = [
                {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'old_price': product.old_price
                } for product in self.all_products
            ]
            return result
        else:
            db_product_all = self.session.execute(self.match_product_name(product_id)).scalars().all()
            if not db_product_all:
                return 'Coming soon'
            return db_product_all

    def select_genres(self):
        result = self.all_genres.all()
        return result
