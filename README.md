# Full Stack NBA players API Backend

## About
RESTful API with Auth0 RBAC to access/modify NBA games and players. Fans can get all endpoints and Managers can get/post/patch/delete. Deployed flask app using Heroku and PostgreSQL.

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

#### GET /players (Authorization: Fans and Managers)
- General:
    - Get all players. Returns a success value, first name, last name and team of players.
- Sample: 
```curl -X GET \
      https://players-games-nba.herokuapp.com/players \
      -H 'Authorization: Bearer <TOKEN>'
```
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

#### GET /questions/?page=<page_number>
- General:
    - Get all questions. Returns paginated (10 per page) list of question objects, total number of questions, list of category objects and success value
- Sample: ```curl http://127.0.0.1:5000/questions```
```
{
   "questions" : [
      {
         "difficulty" : 4,
         "question" : "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
         "category" : 5,
         "answer" : "Apollo 13",
         "id" : 2
      },
      {
         "difficulty" : 4,
         "question" : "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
         "category" : 5,
         "id" : 4,
         "answer" : "Tom Cruise"
      },
      {
         "id" : 5,
         "answer" : "Maya Angelou",
         "difficulty" : 2,
         "question" : "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
         "category" : 4
      },
      {
         "question" : "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
         "difficulty" : 3,
         "category" : 5,
         "answer" : "Edward Scissorhands",
         "id" : 6
      },
      {
         "category" : 4,
         "question" : "What boxer's original name is Cassius Clay?",
         "difficulty" : 1,
         "answer" : "Muhammad Ali",
         "id" : 9
      },
      {
         "id" : 10,
         "answer" : "Brazil",
         "difficulty" : 3,
         "question" : "Which is the only team to play in every soccer World Cup tournament?",
         "category" : 6
      },
      {
         "question" : "Which country won the first ever soccer World Cup in 1930?",
         "difficulty" : 4,
         "category" : 6,
         "answer" : "Uruguay",
         "id" : 11
      },
      {
         "difficulty" : 2,
         "question" : "Who invented Peanut Butter?",
         "category" : 4,
         "id" : 12,
         "answer" : "George Washington Carver"
      },
      {
         "question" : "What is the largest lake in Africa?",
         "difficulty" : 2,
         "category" : 3,
         "answer" : "Lake Victoria",
         "id" : 13
      },
      {
         "answer" : "Agra",
         "id" : 15,
         "question" : "The Taj Mahal is located in which Indian city?",
         "difficulty" : 2,
         "category" : 3
      }
   ],
   "total_questions" : 18,
   "categories" : {
      "4" : "History",
      "2" : "Art",
      "5" : "Entertainment",
      "1" : "Science",
      "3" : "Geography",
      "6" : "Sports"
   },
   "success" : true
}
```

#### DELETE /questions/<int:question_id>
- General:
    - Deletes an existing question with given ID. Returns deleted id, list of questions objects, success value and number of remaining questions.
- Sample: ```curl -X DELETE http://127.0.0.1:5000/questions/4```
```
{
  "deleted": 4, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "total_questions": 17
}
```

#### POST /questions
- General:
    - Creates a new question with given inputs. Returns success value, question id, paginated list of question objects and number of total questions.
- Sample: ```curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "What time is it", "answer": "None of your business", "difficulty": "4", "category": "1"}'```
```
{
  "created": 52, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "total_questions": 18
}
```

#### POST /questions/search
- General:
    - Search questions based on a search term. Returns any questions for whom the search term is a substring of the question.
- Sample: ```curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm": "time"}'```
```
{
  "questions": [
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "None of your business", 
      "category": 1, 
      "difficulty": 4, 
      "id": 52, 
      "question": "What time is it"
    }
  ], 
  "success": true, 
  "total_questions": 2
}
```

#### GET /categories/<int:category_id>/questions
- General:
    - Fetches questions from a given category. Returns current category, list of question objects, success value and total number of questions.
- Sample: ```curl http://127.0.0.1:5000/categories/3/questions```
```
{
  "current_category": 3, 
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "a lot", 
      "category": 3, 
      "difficulty": 5, 
      "id": 25, 
      "question": "how much woud could a wood chuck chuck if it could chuck wood?"
    }
  ], 
  "success": true, 
  "total_questions": 3
}
```

#### POST /quizzes
- General:
    - Returns a random question within a given category that is not one of the previous questions. Returns success value and a list of a question object.
- Sample: ```curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"type": "Science", "id": "1"}}'```
```
{
  "question": {
    "answer": "The Liver", 
    "category": 1, 
    "difficulty": 4, 
    "id": 20, 
    "question": "What is the heaviest organ in the human body?"
  }, 
  "success": true
}
```

## Deployment N/A

## Authors
Eugene

## Acknowledgments
Udacity!
