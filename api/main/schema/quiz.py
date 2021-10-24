from api.main import ma
from flask_marshmallow.fields import fields

from api.main.models.quiz import Quiz


class QuizSchema(ma.Schema):
    class Meta:
        model = Quiz

    # id = fields.Integer()
    title = fields.Str()
    subtitle = fields.Str()
    icon = fields.Str()
    # _links = ma.Hyperlinks(
    #     {
    #         "self": ma.URLFor("quiz", values=dict(id="<id>")),
    #         "collection": ma.URLFor("quizzes"),
    #     }
    # )
