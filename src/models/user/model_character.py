from .. import db;

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    height = db.Column(db.String, nullable=False)
    mass = db.Column(db.String, nullable=False)
    hair_color = db.Column(db.String, nullable=False)
    skin_color = db.Column(db.String, nullable=False)
    eye_color = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime)
    edited = db.Column(db.DateTime)
    favorites = db.relationship('Favorites', backref='character', lazy=True)