from flask import request
from flask_restplus import Resource

from api.main.schema.quiz import QuizSchema
from api.main.service.question_service import QuestionService
from api.main.service.quiz_service import QuizService
from api.main.util.dto import QuizDto

api = QuizDto.api
_quiz = QuizDto.quiz

quiz_schema = QuizSchema()
quizzes_schema = QuizSchema(many=True)


@api.route('/')
class QuizList(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._quiz_service = QuizService()
        self._question_service = QuestionService()

    @api.doc('list_of_registered_quizzes')
    @api.marshal_list_with(_quiz, envelope='data')
    def get(self):
        """List all registered quizzes"""
        quizzes = self._quiz_service.get_all_quizzes()
        return quizzes_schema.dump(quizzes)

    @api.doc('list_questions_for_quiz')
    @api.marshal_list_with(_quiz, envelope='data')
    def get_questions_for_quiz(self, quiz_id):
        return self._question_service.get_questions_for_quiz(quiz_id)

    @api.response(201, 'Quiz successfully created.')
    @api.doc('create a new quiz')
    @api.expect(_quiz, validate=True)
    def post(self):
        """Creates a new Quiz """
        data = request.json
        return self._quiz_service.save_new_quiz(data=data)
