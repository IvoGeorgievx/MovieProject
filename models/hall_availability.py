from db import db


class HallAvailability(db.Model):
    __tablename__ = 'hall_availability'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    movie = db.relationship('Movie')
    hall_id = db.Column(db.Integer, db.ForeignKey('hall.id'), nullable=False)
    hall = db.relationship('Hall', backref=db.backref('availability', lazy=True))
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
