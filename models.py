from sqlalchemy import Column, String, create_engine, Integer, Date
from flask_sqlalchemy import SQLAlchemy
from config import database_params
from datetime import date
import json
import os

# try to get heroku DATABASE_URL env variable
# or set default local db connection string
database_path = os.environ.get('DATABASE_URL',
                               "{}://{}:{}@localhost:5432/{}".format(
                                   database_params["dialect"],
                                   database_params["username"],
                                   database_params["password"],
                                   database_params["db_name"]))

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''


def db_drop_and_create_all():
    #db.drop_all()
    db.create_all()
    db_populate_db()


'''
db_populate_db()
  populate the db with dummy data
'''


def db_populate_db():
    new_singer_1 = Singer('Joao Gilberto', 'Male', '90')
    new_singer_2 = Singer('Seu Jorge', 'Male', '58')
    new_singer_3 = Singer('Maria Bethania', 'Female', '62')

    new_song_1 = Song('Samba do Bencao', date.today())
    new_song_2 = Song('De Todas as Maneiros', date.today())

    new_singer_1.insert()
    new_singer_2.insert()
    new_singer_3.insert()

    new_song_1.insert()
    new_song_2.insert()

    new_performance_1 = Performance.insert().values(
        song_id=new_song_1.id, singer_id=new_singer_1.id)
    new_performance_2 = Performance.insert().values(
        song_id=new_song_2.id, singer_id=new_singer_2.id)
    new_performance_3 = Performance.insert().values(
        song_id=new_song_2.id, singer_id=new_singer_3.id)

    db.session.execute(new_performance_1)
    db.session.execute(new_performance_2)
    db.session.execute(new_performance_3)
    db.session.commit()


'''
Performance
N:N relationship between movies and actors
'''
Performance = db.Table('performance', db.Model.metadata,
                       db.Column('song_id', db.Integer,
                                 db.ForeignKey('song.id')),
                       db.Column('singer_id', db.Integer,
                                 db.ForeignKey('singer.id')))


'''
Movie
Have a title and release year
'''


class Song(db.Model):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)
    singer = db.relationship('Singer', secondary=Performance,
                             backref=db.backref('performances', lazy='joined'))

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'actors': [singer.name for singer in self.singer]}

    '''
  insert()
      inserts a new model into a database
  '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
  delete()
      deletes a new model into a database
      the model must exist in the database
  '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
  update()
      updates a new model into a database
      the model must exist in the database
  '''

    def update(self):
        db.session.commit()


'''
Actor
Have a name, age and gender
'''


class Singer(db.Model):
    __tablename__ = 'singer'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    age = Column(Integer)

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age}

    '''
  insert()
      inserts a new model into a database
  '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
  delete()
      deletes a new model into a database
      the model must exist in the database
  '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
  update()
      updates a new model into a database
      the model must exist in the database
  '''

    def update(self):
        db.session.commit()