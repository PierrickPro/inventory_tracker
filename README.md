# inventory_tracker

## Running The Project

[Python](https://www.python.org/downloads/) (3.8.9 or later) is required to run this project.

1. Install [poetry](https://python-poetry.org/docs/)

2. Clone this repository on your computer

3.  run the following commands from the repo's root directory:
```
poetry --version # make sure poetry was successfully installed
poetry install
export FLASK_APP=app/run.py
python -m flask run
```
The project is now running: ```* Running on http://... ```

4. Copy the URL given and paste it in your web browser


## Database Settings

- By default, the project will use sqlite. A file called 'db.sqlite' will be created to store the tables when you first run the app<br>
- You can change SQLALCHEMY_DATABASE_URI in config.py to use another database, such as PostgreSQL (postgresql://...)

