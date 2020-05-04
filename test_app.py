import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import Player, Game, db, setup_db
from flask import Flask
from app import create_app

MANAGER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Inh5NHpGUk9sV2dBbmhBaFZEbW92YSJ9.eyJpc3MiOiJodHRwczovL2V1Z2VuZWxlZS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5Yjk0YTI2M2Y4MDAwYzhjMjE1MjdlIiwiYXVkIjoibmJhIiwiaWF0IjoxNTg4NTQ4Nzc2LCJleHAiOjE1ODg2MjA3NzYsImF6cCI6IlM2algzNWxBS0xwVlFMVUFwZ2ZJbUxUdjBwRzBnR3pjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cmVxdWVzdHMiLCJnZXQ6cmVxdWVzdHMiLCJwYXRjaDpyZXF1ZXN0cyIsInBvc3Q6cmVxdWVzdHMiXX0.X6Biqawmhwc-QP8CificEEhtqApMZmydA5kkUaNoJHqOMVLaLka2_otYNwKTbPNhLLRaW90H_Iq9nPPCfrOPVbrBgAnyCshe8kL37zwGwlg0_UbjOIK5tL6yatKj3425j0GMm7zme65FVrS444o25k8sMmnYYkVcgEiqIRu9A-WtwRcgair8y0Krt0VCi06g-3X4Xygn8551pLkdx9l1W_CbJjDGBRK0vmcOrSrvpnMKShgH5LKSMQLRLOQgNzpcSU9qOmKfUN4c1OKE-w4cHHljSTY3OUT62qKYH-oR1XbTm-bm6R8eIBVQ3J6yiYUrN80UZBMFf0DLGHjxus6ppg'

class TestCases(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.database_name = "basketball_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.client = self.app.test_client()
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
        res = self.client.post('/players', json=new_player, headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)


    def test_401_get_players(self):
        res = self.client.get('/players')
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 401)


    def test_get_players(self):
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
        player = Player(first="Ryo", last="Tawatari", team="YOKOHAMA B-CORSAIRS")
        player.insert()
        player_id = player.id

        updated_player = {
            "first": "anthony",
            "last": "davis",
            "team": "lakers"
        }

        self.headers.update({'Authorization': 'Bearer ' + MANAGER_TOKEN})
        res = self.client.patch(f'/players/{player_id}', json=updated_player, headers=self.headers)
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
