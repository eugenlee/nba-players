import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import Player, Game, db, setup_db
from flask import Flask
from app import create_app

MANAGER_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Inh5NHpGUk9sV2dBbmhBaFZEbW92YSJ9.eyJpc3MiOiJodHRwczovL2V1Z2VuZWxlZS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWU5Yjk0YTI2M2Y4MDAwYzhjMjE1MjdlIiwiYXVkIjoibmJhIiwiaWF0IjoxNTg4NTY1ODA1LCJleHAiOjE1ODg2Mzc4MDUsImF6cCI6IlM2algzNWxBS0xwVlFMVUFwZ2ZJbUxUdjBwRzBnR3pjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cmVxdWVzdHMiLCJnZXQ6cmVxdWVzdHMiLCJwYXRjaDpyZXF1ZXN0cyIsInBvc3Q6cmVxdWVzdHMiXX0.HYbsU4y_ah2_S6sA585pt--YCJpSBOvpi8hT14ypiYrEPpYQ2IYSOrI09yuwUcTiKwLYHvYLEiMkoO8qUl1dMZ_u73x6qfEBnA2se8zFCnJnOMR9qvrWaA_30116FsykTdkHNbKcCw9IXH7aZwgv79z4Rdl88rW4K2-JdwHpPXISx1i9Yhm3CiKzIxWYsQpwWmThuQGI7nhKJVnTn0grMS0CCaUH6g7FsMQQuk4gyFFYCCpg5B5EZnpuO2Logwd2RKbCsH9R27Ce0FaaKHSC1LgF8bPupayLiwv5p6oWuV_-p6qMuTxx3F-GHVaEasAKRnQ8fcyj_JjeH9t2DI2Y3A'
FAN_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Inh5NHpGUk9sV2dBbmhBaFZEbW92YSJ9.eyJpc3MiOiJodHRwczovL2V1Z2VuZWxlZS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVhNjI0YmU1NGIxNGMwYzEyNTllZTEwIiwiYXVkIjoibmJhIiwiaWF0IjoxNTg4NTY2MDQzLCJleHAiOjE1ODg2MzgwNDMsImF6cCI6IlM2algzNWxBS0xwVlFMVUFwZ2ZJbUxUdjBwRzBnR3pjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6cmVxdWVzdHMiXX0.M4GCl_PxUn8IhSsOsOc38X2sOZ_C__UG6-OQrap5e7P657REMdZ6G3jMTVTvh-DMJ3LN1bch5BfaMyiKHwRkg1Ms9EWgb1UOJ9IQ853RUX1h1Q52aCN28x2qDvvOSWnqlcAzJDLUZ1gAHXo4GnIJCHVJtYo9G8waRs_SV79J-Dt8b9_vq2kO8EJEYSmfFQ4IhQnuzwolFVJR4QQMZ1kGn0eniKakTObUeBoSMRHAHi54uAjrDVNPgrNWozkd38Ru-Ph4uz2qjRG0thCoXoSaYaOcsloiGfywKb-0PFFp_6lP7EYV3xNSW6zm4d5dlaSjo2Lcr0YnPwEjeVTSW1ARMQ'

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
