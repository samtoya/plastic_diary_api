import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app
from api.main.config import basedir


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('api.main.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'] == True)
        self.assertFalse(current_app == None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir,
                                                                                 'plastic_dairy_development.sqlite')
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('api.main.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' + os.path.join(basedir, 'plastic_dairy_test.sqlite')
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('api.main.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] == False)


if __name__ == '__main__':
    unittest.main()
