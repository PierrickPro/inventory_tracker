# inventory_tracker

## Running The Project

[Python](https://www.python.org/downloads/) (3.8.9 or later) is required to run this project.

1. Clone this repository on your computer

2.  run the following commands from the repo's root directory:
```
pip install -r requirements.txt
export FLASK_APP=app/run.py
python -m flask run
```
The project is now running: ```* Running on http://... ```

3. Copy the URL given and paste it in your web browser


## Database Settings

- By default, the project will use sqlite. A file called 'db.sqlite' will be created to store the tables when you first run the app<br>
- You can change SQLALCHEMY_DATABASE_URI in config.py to use another database, such as PostgreSQL (postgresql://...)

