import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import Player, Game, db, setup_db
from flask import Flask
from app import create_app

MANAGER_TOKEN = ("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Inh5NHpGUk9s"
                "V2dBbmhBaFZEbW92YSJ9.eyJpc3MiOiJodHRwczovL2V1Z2VuZWxlZS5h"
                "dXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5Yjk0YTI2M2Y4MDAwYzhjM"
                "jE1MjdlIiwiYXVkIjoibmJhIiwiaWF0IjoxNTg4NjA3ODM4LCJleHAiOj"
                "E1ODg2Nzk4MzgsImF6cCI6IlM2algzNWxBS0xwVlFMVUFwZ2ZJbUxUdjB"
                "wRzBnR3pjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6"
                "cmVxdWVzdHMiLCJnZXQ6cmVxdWVzdHMiLCJwYXRjaDpyZXF1ZXN0cyIsI"
                "nBvc3Q6cmVxdWVzdHMiXX0.hZlpTffGoSvMsnakQPzYrwgGfqXgStbf68"
                "xP7W6n3ez14oD_kg3SW5f5R3KOq72WKoMFxoGe2alxO1qqKZlM2weFRJm"
                "-zt2ioc5TP_TGMGDSK-6THkfqWwJ1ZjMeG8_HL_hsl2Pr_uJstQ2-AChL"
                "b4YhOxDb6gMhGLulqI_QWk9SjXmMEYerCud9a_bRjgRuOVY5RkcyXcRv2"
                "w-oiQtX4ijNRVGHlvuoi5eAmhJzpWIw9Kx8LtYtjBlXR3igMj1Uw1qWNG"
                "DxMIiQO66GfCr3SoWbmAhWE_8A_QnUaFWdLCJUr9NjfabdzkrrUMtaEYp"
                "V8OmGanuvUESIgkmPzdLm5Q")
FAN_TOKEN = ("eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Inh5NHpGUk9sV2dB"
            "bmhBaFZEbW92YSJ9.eyJpc3MiOiJodHRwczovL2V1Z2VuZWxlZS5hdXRoMC5j"
            "b20vIiwic3ViIjoiYXV0aDB8NWVhNjI0YmU1NGIxNGMwYzEyNTllZTEwIiwiY"
            "XVkIjoibmJhIiwiaWF0IjoxNTg4NjA3OTY5LCJleHAiOjE1ODg2Nzk5NjksIm"
            "F6cCI6IlM2algzNWxBS0xwVlFMVUFwZ2ZJbUxUdjBwRzBnR3pjIiwic2NvcGU"
            "iOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6cmVxdWVzdHMiXX0.YNVisj1UX7o_"
            "kmdin8dUmxrwNalZKy103hKJJ6FwiyY8dTS_X445mRBh1mMJmIHrOjebgxx14"
            "ab2gsPhjrrt5lcIx3XD_XN2vCiLwDcjWPHlXPTXe997t1hn3dz-zucsyO90gn"
            "l_wfhJ3uasyVKFlQhk9YQLiR_z4fOTV0ZDveoDoyTYyecY0AqWr55a_-d9e-Z"
            "eUmuGIlUPGWCXySy9ab2t0ZCF_wtg737BIuSXafFnklt4npJJ6WjGTDKgv7uh"
            "VQolbhyCFLqRIzEFGyt-OUvwGo9Y7mDzKz6mQzumdaUm_ucGFH4NRHWJnyFsh"
            "es8yLaSqJg3t0AU3m1YIPN88w")


class TestCases(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.database_name = "basketball_test"
        self.database_path = "postgresql://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.headers = {'Content-Type': 'application/json'}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_401_new_player(self):
        new_player = {
            "first": "lebron",
            "last": "james",
            "team": "lakers"
        }

        res = self.client.post('/players', json=new_player)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)

    def test_new_player(self):
        new_player = {
            "first": "lebron",
            "last": "james",
            "team": "lakers"
        }
        self.headers.update({'Authorization': 'Bearer ' + MANAGER_TOKEN})
        res = self.client.post(
            '/players', json=new_player, headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    def test_401_get_players(self):
        res = self.client.get('/players')
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)

    def test_fan_get_players(self):
        self.headers.update({'Authorization': 'Bearer ' + FAN_TOKEN})
        res = self.client.get('/players', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    def test_manager_get_players(self):
        self.headers.update({'Authorization': 'Bearer ' + MANAGER_TOKEN})
        res = self.client.get('/players', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    def test_401_new_game(self):
        new_game = {
            "home_away": "home",
            "venue": "staples",
        }

        res = self.client.post('/games', json=new_game)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)

    def test_new_game(self):
        new_game = {
            "home_away": "home",
            "venue": "staples",
        }

        self.headers.update({'Authorization': 'Bearer ' + MANAGER_TOKEN})
        res = self.client.post('/games', json=new_game, headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    def test_401_get_games(self):
        res = self.client.get('/games')
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)

    def test_get_games(self):
        self.headers.update({'Authorization': 'Bearer ' + MANAGER_TOKEN})
        res = self.client.get('/games', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    def test_401_update_player(self):
        updated_player = {
            "first": "anthony",
            "last": "davis",
            "team": "lakers"
        }

        res = self.client.patch('/players/1', json=updated_player)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)

    def test_update_player(self):
        player = Player(first="Ryo", last="Tawatari",
                        team="YOKOHAMA B-CORSAIRS")
        player.insert()
        player_id = player.id

        updated_player = {
            "first": "anthony",
            "last": "davis",
            "team": "lakers"
        }

        self.headers.update({'Authorization': 'Bearer ' + MANAGER_TOKEN})
        res = self.client.patch(
            f'/players/{player_id}', json=updated_player, headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    def test_401_delete_player(self):
        res = self.client.delete('/players/1')
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)

    def test_delete_player(self):
        player = Player(first="danny", last="cook", team="lakers")
        player.insert()
        player_id = player.id

        self.headers.update({'Authorization': 'Bearer ' + MANAGER_TOKEN})
        res = self.client.delete(f'/players/{player_id}', headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
