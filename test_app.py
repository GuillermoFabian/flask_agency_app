import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Singer, Song, db_drop_and_create_all
from config import auth0_tokens, database_params


# Assign testing authorization headers

assistant_auth_header = {
    'Authorization': "Bearer " + auth0_tokens["assistant"]
}

manager_auth_header = {
    'Authorization': "Bearer " + auth0_tokens["manager"]
}

owner_auth_header = {
    'Authorization': "Bearer " + auth0_tokens["owner"]
}

# database path
database_path = os.environ.get('DATABASE_URL',
                               "{}://{}:{}@localhost: 5432/{}".format(
                                   database_params["dialect"],
                                   database_params["username"],
                                   database_params["password"],
                                   database_params["db_name"]))


class DiscographyTestCase(unittest.TestCase):
    """This class represents the test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        setup_db(self.app, self.database_path)
        db_drop_and_create_all()

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # test cases
    # test get singer
    def test_get_singer(self):
        res = self.client().get('/singer',
                                headers=owner_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['singers']))

    # test get songs
    def test_get_song(self):
        res = self.client().get('/song',
                                headers=owner_auth_header)
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['songs']))

    # test create singer

    def test_create_singer(self):
        new_singer = {'name': 'New_Singer_1', 'age': '30',
                     'gender': 'Male'}
        res = self.client().post('/singer', json=new_singer,
                                 headers=owner_auth_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_422_create_singer(self):
        new_singer = {}
        res = self.client().post('/singer', json=new_singer,
                                 headers=owner_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            """Unprocessable Entity.
            An error occured while processing your request""")

    # test create song
    def test_create_song(self):
        new_song= {'title': 'New_Song_1',
                     'release_date': '12/6/2021'}
        res = self.client().post('/song', json=new_song,
                                 headers=owner_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_422_create_song(self):
        new_song= {}
        res = self.client().post('/song', json=new_song,
                                 headers=owner_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            """Unprocessable Entity.
            An error occured while processing your request""")

# test delete singer
    def test_delete_singer(self):
        res = self.client().delete('/singer/1', headers=owner_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)

    def test_422_delete_singer(self):
        res = self.client().delete('/singer/400', headers=owner_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            """Unprocessable Entity.
            An error occured while processing your request""")

    # test delete song
    def test_delete_song(self):
        res = self.client().delete('/song/1', headers=owner_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)

    def test_422_delete_song(self):
        res = self.client().delete('/song/400', headers=owner_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            """Unprocessable Entity.
            An error occured while processing your request""")

    # test update singer

    def test_update_singer(self):
        update_singer= {'name': 'Mohamed Khalaf'}
        res = self.client().patch('/singer/2', json=update_singer,
                                  headers=owner_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_422_update_singer(self):
        update_singer = {}
        res = self.client().patch('/singer/2', json=update_singer,
                                  headers=owner_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            """Unprocessable Entity.
            An error occured while processing your request""")

    # test update song

    def test_update_song(self):
        update_song = {'title': 'UPDATE_NAME', 'release_dat': '12/6/2020'
                        }
        res = self.client().patch('/song/2', json=update_song,
                                  headers=owner_auth_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_422_update_song(self):
        update_song = {}
        res = self.client().patch('/song/2', json=update_song,
                                  headers=owner_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'],
            """Unprocessable Entity.
            An error occured while processing your request""")

    # RBAC remaining tests
    # assistant
    def test_get_singer_assistant(self):
        res = self.client().get('/singer',
                                headers=assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['singers']))

    def test_update_song_assistant(self):
        update_song = {'title': 'UPDATE_NAME', 'release_dat': '12/6/2020'
                        }
        res = self.client().patch('/song/2', json=update_song,
                                  headers=assistant_auth_header)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], "Permission not found.")

    def test_create_song_assistant(self):
        new_song = {'title': 'New_Song_1', 'release_date': '12/6/2020'}
        res = self.client().post('/song', json=new_song,
                                 headers=assistant_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], "Permission not found.")

    # Manager
    def test_get_singer_manager(self):
        res = self.client().get('/singer',
                                headers=manager_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['singers']))

    def test_create_song_manager(self):
        new_song = {'title': 'New_Song_1', 'release_date': '12/6/2020'}
        res = self.client().post('/song', json=new_song,
                                 headers=manager_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], "Permission not found.")

    def test_delete_song_manager(self):
        res = self.client().delete('/song/1',
                                   headers=manager_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(
            data['message'], "Permission not found.")

    # Executive producer RBAC tests are covered above


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
