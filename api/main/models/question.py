import datetime

from .quiz import Quiz
from .. import db


class Question(db.Model):
    """ Question Model for storing question related details """
    __tablename__ = "questions"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
    text = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    quiz = db.relationship(Quiz, backref='questions', lazy=True)
