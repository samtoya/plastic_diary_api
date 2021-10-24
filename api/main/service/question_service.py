from api.main import db
from api.main.models.question import Question


class QuestionService:
    def get_all_questions(self):
        return Question.query.all()

    def get_questions_for_quiz(self, quiz_id):
        return Question.query.filter_by(question_id=quiz_id).all()

    def get_a_question(self, question_id):
        return Question.query.filter_by(id=question_id).first()

    def save_new_question(self, data):
        quiz = Question.query.filter_by(
            title=data['text']
        ).first()
        if not quiz:
            new_quiz = Question(
                text=data['title'],
            )
            self.save_changes(new_quiz)
        else:
            response_object = {
                'status': 'fail',
                'message': 'Question already exists',
                'quiz': quiz
            }
            return response_object, 409

    def save_changes(self, data):
        db.session.add(data)
        db.session.commit()
