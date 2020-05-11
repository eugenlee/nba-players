# Full Stack NBA players API Backend

## About
RESTful API with Auth0 RBAC to access/modify NBA games and players. Fans can get all endpoints and Managers can get/post/patch/delete. Deployed flask app using [Heroku](https://players-games-nba.herokuapp.com/) and PostgreSQL.

#### Other projects within this course
1. [fyyur](https://github.com/eugenlee/fyyur)
2. [trivia](https://github.com/eugenlee/trivia)
3. [coffeeshop](https://github.com/eugenlee/coffeeshop)
4. [flask_kubernetes](https://github.com/eugenlee/flask_kubernetes)

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

It's recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/nba-players` project folder and running:

```bash
pip install -r requirements.txt
```
To test locally, set up environmental variable:
```bash
source setup.sh 
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Database Setup
With Postgres running, create a database:
```bash
createdb basketball
```

## Running the server

From within the project folder first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## Testing
To run the tests, run
```
dropdb basketball_test
createdb basketball_test
python3 test_app.py
```

## API Reference

### Getting Started

- Base URL: At present this app can be run locally and is hosted on [Heroku](https://players-games-nba.herokuapp.com/). The backend app is hosted at the default, ```http://127.0.0.1:5000/```, which is set as a proxy in the frontend configuration.
- Authentication: Tokens for 2 roles provided in test_app.py.

### Roles and Permissions
There are 2 roles within the API
- Fan:
    - Can view players and games
- Manager:
    - All permissions that Fans have and...
    - Add players
    - Update players
    - Delete players
    - Add games

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 404,
    "message": "Not found"
}
```
The API will return three error types when requests fail:
- 404: Resource Not Found
- 422: Not Processable
- 401: Authorization error

### Endpoints

#### GET / (Authorization: None)
- General:
    - Login screen. Returns a success value.
- Sample:
```
{
    "success": true
}
```

#### GET /players (Authorization: Fan and Manager)
- General:
    - Get all players. Returns a success value, first name, last name and team of players.
- Sample: 
```
curl -X GET \
  https://players-games-nba.herokuapp.com/players \
  -H 'Authorization: Bearer <TOKEN>'
```
- Response:
```
{
    "players": [
        {
            "firstname": "lebron",
            "id": 2,
            "lastname": "james",
            "team": "lakers"
        },
        {
            "firstname": "steph",
            "id": 3,
            "lastname": "curry",
            "team": "warriors"
        },
        {
            "firstname": "seth",
            "id": 4,
            "lastname": "curry",
            "team": "mavericks"
        }
    ],
    "success": true
}
```

#### GET /games (Authorization: Fan and Manager)
- General:
    - Get all games. Returns a success value, home or away value and venue.
- Sample: 
```
curl -X GET \
  https://players-games-nba.herokuapp.com/games \
  -H 'Authorization: Bearer <TOKEN>'
```
- Response
```
{
    "games": [
        {
            "home_away": "home",
            "id": 1,
            "venue": "staples"
        },
        {
            "home_away": "away",
            "id": 2,
            "venue": "oracle"
        },
        {
            "home_away": "away",
            "id": 3,
            "venue": "msg"
        },
        {
            "home_away": "away",
            "id": 4,
            "venue": "united"
        }
    ],
    "success": true
}
```

#### POST /players (Authorization: Manager)
- General:
    - Posts new player. Returns success value.
- Sample: 
```
curl -X POST \
  https://players-games-nba.herokuapp.com/players \
  -H 'Authorization: Bearer <TOKEN>' \
  -H "Content-Type: application/json" \
  -d '{"first": "jayson", "last": "tatum", "team": "boston"}'
```
- Response:
```
{
    "success": true
}
```

#### PATCH /players/<int:id> (Authorization: Manager)
- General:
    - Updates existing player with given ID. Returns success value.
- Sample: 
```
curl -X PATCH \
  https://players-games-nba.herokuapp.com/players/4 \
  -H 'Authorization: Bearer <TOKEN>' \
  -H "Content-Type: application/json" \
  -d '{"first": "kawhi", "last": "leonard", "team": "clippers"}'
```
- Response:
```
{
    "success": true
}
```

#### DELETE /players/<int:id> (Authorization: Manager)
- General:
    - Deletes existing player with given ID. Returns success value and ID of deleted player.
- Sample: 
```
curl -X DELETE \
  https://players-games-nba.herokuapp.com/players/6 \
  -H 'Authorization: Bearer <TOKEN>' 
```
- Response:
```
{
    "success": true,
    "id": 6
}
```

#### POST /games (Authorization: Manager)
- General:
    - Posts new game. Returns success value.
- Sample: 
```
curl -X POST \
  https://players-games-nba.herokuapp.com/games \
  -H 'Authorization: Bearer <TOKEN>' \
  -H "Content-Type: application/json" \
  -d '{"home_away": "away", "venue": "sleep train"}'
```
- Response:
```
{
    "success": true
}
```

## Deployment N/A

## Authors
Eugene

## Acknowledgments
Thanks to Udacity for a great program!
