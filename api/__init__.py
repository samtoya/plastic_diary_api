from flask_restplus import Api
from flask import Blueprint

from .main.controllers.user_controller import api as user_ns
from .main.controllers.auth_controller import api as auth_ns
from .main.controllers.quiz_controller import api as quiz_ns
from .main.controllers.question_controller import api as question_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Plastic Diary REST API',
          version='1.0',
          description='A flask restful microservice application for the diary application.'
          )

# api.add_namespace(user_ns, path='/user')
api.add_namespace(quiz_ns, path='/v1/quizzes')
api.add_namespace(auth_ns, path='/v1/auth')
api.add_namespace(question_ns, path='/v1/questions')
