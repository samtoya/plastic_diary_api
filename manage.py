import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from api import blueprint
from api.main import create_app, db

app = create_app(os.getenv('ENV') or 'development')
app.register_blueprint(blueprint)
app.app_context().push()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('api/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
