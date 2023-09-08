from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)))
    shows = db.relationship('Show', backref='Venue', lazy=True, cascade='all, delete-orphan')
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(500))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

    #implementing the cout of past and future shows
    @property
    def upcoming_shows(self):
        # upcoming_shows = Show.query.filter(Show.start_time > datetime.now(), Show.venue_id==self.id)
        upcoming_shows=db.session.query(Show).join(Venue).filter(Show.venue_id==self.id).filter(
            Show.start_time > datetime.now()
        )
        return upcoming_shows
    @property
    def upcoming_showsCount(self):
        return self.upcoming_shows.count()

    @property
    def past_shows(self):
        past_shows=db.session.query(Show).join(Venue).filter(Show.venue_id==self.id).filter(
            Show.start_time < datetime.now()
        )
        return past_shows

    @property
    def past_showsCount(self):
        return self.past_shows.count()


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref='Artist', lazy=True)
    seeking_venue = db.Column(db.Boolean, default=False, nullable=False)
    seeking_description = db.Column(db.String(500))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    #implementing the past and future shows with respect to artists
    @property
    def upcoming_shows(self):
        # upcoming_shows = Show.query.filter(Show.start_time > datetime.now(), Show.artist_id==self.id)
        upcoming_shows=db.session.query(Show).join(Venue).filter(Show.artist_id==self.id).filter(
            Show.start_time > datetime.now()
        )
        return upcoming_shows
    @property
    def upcoming_showsCount(self):
        return self.upcoming_shows.count()

    @property
    def past_shows(self):
        # past_shows = Show.query.filter(Show.start_time < datetime.now(), Show.artist_id==self.id)
        past_shows=db.session.query(Show).join(Venue).filter(Show.artist_id==self.id).filter(
            Show.start_time < datetime.now()
        )
        return past_shows

    @property
    def past_showsCount(self):
        return self.past_shows.count()

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)