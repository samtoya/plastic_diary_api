from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('User', description='User operations.')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('Authentication', description='Authentication operations.')
    user_auth = api.model('credential', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class QuizDto:
    api = Namespace('Quiz', description='Quiz operations.')
    quiz = api.model('quiz', {
        'title': fields.String(required=True, description='The title of the quiz'),
        'subtitle': fields.String(description='The subtitle of the quiz'),
        'icon': fields.String(description='The icon url of the quiz'),
    })


class QuestionDto:
    api = Namespace('Question', description='Question operations.')
    question = api.model('question', {
        'text': fields.String(required=True, description='The question'),
    })
