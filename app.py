import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Player, Game, db, setup_db
from auth import AuthError, requires_auth

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    # general access

    @app.route("/players", methods=['GET'])
    @requires_auth('get:requests')
    def get_players(jwt):
        try:
            players = Player.query.all()

            return jsonify({
                'success': True,
                'players': [player.formatter() for player in players]
            })

        except:
            abort(404)


    @app.route("/games", methods=['GET'])
    @requires_auth('get:requests')
    def get_games(jwt):
        try:
            games = Game.query.all()
            
            return jsonify({
                'success': True,
                'games': [game.formatter() for game in games]
            })

        except:
            abort(404)


    # players with authorization

    @app.route("/players", methods=['POST'])
    @requires_auth('post:requests')
    def add_player(jwt):

        body = request.get_json()
        if not ('first' in body and 'last' in body and 'team' in body):
            abort(404)

        first = body.get('first')
        last = body.get('last')
        team = body.get('team')

        try:
            player = Player(first=first, last=last, team=team)
            player.insert()

            return jsonify({
                'success': True
            })

        except:
            abort(422)


    @app.route("/players/<id>", methods=['PATCH'])
    @requires_auth('patch:requests')
    def update_player(jwt, id):

        player = Player.query.get(id)

        if player:
            try:
                body = request.get_json()

                first = body.get('first')
                last = body.get('last')
                team = body.get('team')

                if first:
                    player.first = first
                if last:
                    player.last = last
                if team:
                    player.team = team

                player.update()

                return jsonify({
                    'success': True
                })

            except:
                abort(422)
        else:
            abort(404)


    @app.route("/players/<id>", methods=['DELETE'])
    @requires_auth('delete:requests')
    def delete_player(jwt, id):

        player = Player.query.get(id)

        if player:
            try:
                player.delete()
                return jsonify({
                    'success': True,
                    'delete': id
                })

            except:
                abort(422)
        else:
            abort(404)


    # games with authorization

    @app.route("/games", methods=['POST'])
    @requires_auth('post:requests')
    def add_game(jwt):

        body = request.get_json()

        if not ('home_away' in body and 'venue' in body):
            abort(404)

        home_away = body.get('home_away')
        venue = body.get('venue')

        try:
            game = Game(home_away=home_away, venue=venue)
            game.insert()

            return jsonify({
                'success': True
            })

        except:
            abort(422)


    # errorhandler

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404


    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        return jsonify({
            "success": False,
            "error": ex.status_code,
            'message': ex.error
        }), 401

    return app
