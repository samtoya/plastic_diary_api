from flask_marshmallow.fields import fields

from api.main import ma
from api.main.models.quiz import Quiz


class QuestionSchema(ma.Schema):
    class Meta:
        model = Quiz

    # id = fields.Integer()
    text = fields.Str()
    # _links = ma.Hyperlinks(
    #     {
    #         "self": ma.URLFor("quiz", values=dict(id="<id>")),
    #         "collection": ma.URLFor("quizzes"),
    #     }
    # )
