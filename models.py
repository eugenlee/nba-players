import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

database_path = os.environ.get('DATABASE_URL')

if not database_path:
    database_name = "basketball"
    database_path = "postgres://{}/{}".format('localhost:5432', database_name)

# database_name = "basketball"
# database_path = "postgres://{}/{}".format('localhost:5432', database_name)
# database_heroku = 'postgres://udujxogetfxnml:480c7a67acedd28e943f702083a8bb551001ee03192ba6decde300dd512c176e@ec2-52-87-135-240.compute-1.amazonaws.com:5432/dft3vp8tcgic43'

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(), nullable=False)
    last = db.Column(db.String(), nullable=False)
    team = db.Column(db.String())

    def __init__(self, first, last, team):
        self.first = first
        self.last = last
        self.team = team

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def formatter(self):
        return {
            'id': self.id,
            'firstname': self.first,
            'lastname': self.last,
            'team': self.team,
        }

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    home_away = db.Column(db.String(), nullable=False)
    venue = db.Column(db.String())

    def __init__(self, home_away, venue):
        self.home_away = home_away
        self.venue = venue

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def formatter(self):
        return {
            'id': self.id,
            'home_away': self.home_away,
            'venue': self.venue
        }

    def __repr__(self):
        return '<id {}>'.format(self.id)
