import datetime

from .. import db


class Quiz(db.Model):
    """ Quiz Model for storing user related details """
    __tablename__ = "quizzes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    subtitle = db.Column(db.String, nullable=True)
    icon = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())