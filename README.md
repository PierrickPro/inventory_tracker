# inventory_tracker

## Running The Project

- Clone this repository on your computer

- run the following commands from the repo's root directory:
```
python -m pip install poetry
poetry --version # make sure poetry was successfully installed
poetry install
export FLASK_APP=app/run.py
flask run
```

The project is now running: ```* Running on http://... ```

- Copy the URL given and paste it in your web browser


## Database Settings

- By default, the project will use sqlite. A file called 'db.sqlite' will be created to store the tables when you first run the app<br>
- You can change SQLALCHEMY_DATABASE_URI in config.py to use another database, such as PostgreSQL (postgresql://...)

