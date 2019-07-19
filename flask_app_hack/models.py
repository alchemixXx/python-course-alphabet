import random

from db import db

game_players = db.Table(
    'game_players',
    db.Column('user_id', db.Integer, db.ForeignKey('user_game.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'))
)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secret_number = db.Column(db.Integer, default=random.randint(0, 10))
    attempt = db.Column(db.Integer)
    status = db.Column(db.String, default='active')
    author_id = db.Column(db.Integer, db.ForeignKey('user_game.id'))
    players = db.relationship('GameUser', secondary=game_players, backref=db.backref('players'))
    range_from = db.Column(db.Integer)
    range_to = db.Column(db.Integer)
    winner_id = db.Column(db.Integer, db.ForeignKey('user_game.id'))
    password = db.Column(db.String)


class Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.Integer, db.ForeignKey('user_game.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    numb_of_tries = db.Column(db.Integer)



class GameUser(db.Model):
    __tablename__ = 'user_game'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    role = db.Column(db.String)
