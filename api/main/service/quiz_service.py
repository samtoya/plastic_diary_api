from api.main import db
from api.main.models.quiz import Quiz


class QuizService:
    def get_all_quizzes(self):
        return Quiz.query.all()

    def get_questions_for_quiz(self, quiz_id):
        return

    def save_new_quiz(self, data):
        quiz = Quiz.query.filter_by(
            title=data['title']
        ).first()
        if not quiz:
            new_quiz = Quiz(
                title=data['title'],
                subtitle=data['subtitle'],
                icon=data['icon'],
            )
            self.save_changes(new_quiz)
        else:
            response_object = {
                'status': 'fail',
                'message': 'Quiz already exists',
                'quiz': quiz
            }
            return response_object, 409

    def save_changes(self, data):
        db.session.add(data)
        db.session.commit()
