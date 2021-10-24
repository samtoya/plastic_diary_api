from flask import request
from flask_restplus import Resource

from api.main.schema.question import QuestionSchema
from api.main.service.question_service import QuestionService
from api.main.util.dto import QuestionDto

api = QuestionDto.api
_question = QuestionDto.question

question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)


@api.route('/')
class QuestionList(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._question_service = QuestionService()

    @api.doc('list_of_registered_quizzes')
    @api.marshal_list_with(_question, envelope='data')
    def get(self):
        """List all questions"""
        questions = self._question_service.get_all_questions()
        return questions_schema.dump(questions)

    @api.response(201, 'Quiz successfully created.')
    @api.doc('create a new quiz')
    @api.expect(_question, validate=True)
    def post(self):
        """Creates a new Quiz """
        data = request.json
        return self._question_service.save_new_question(data=data)


@api.route('/<question_id>')
@api.param('question_id', 'The question identifier')
@api.response(404, 'Question not found.')
class Question(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._question_service = QuestionService()

    @api.doc('get a question')
    @api.marshal_with(_question)
    def get(self, question_id):
        """get a question given its identifier"""
        user = self._question_service.get_a_question(question_id)
        if not user:
            api.abort(404)
        else:
            return user
