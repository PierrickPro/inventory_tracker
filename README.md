# inventory_tracker

Inventory tracking web application, with basic CRUD functionalities.<br>
Extra feature implemented: Filtering based on different fields

## Technologies Used

- Python
- HTML
- Jinja
- Flask
- SqlAlchemy
- WTForms

## Running The Project

[Python](https://www.python.org/downloads/) (3.8.9 or later) is required to run this project.

1. Clone this repository on your computer

2. using Terminal (or Command Prompt) run the following commands from the repo's root directory:
```
pip3 install -r requirements.txt
export FLASK_APP=app/run.py # use 'set FLASK_APP=app/run.py" on Windows
python3 -m flask run
```
The project should be running: ```* Running on http://... ```

3. Copy the URL given and paste it in your web browser


## Database Settings

- The project contains a default config file to test the app<br>
- A file called 'db.sqlite' will be created to store tables when you first run the app<br>
- SQLALCHEMY_DATABASE_URI can be modified to use another database, such as a PostgreSQL database (postgresql://...)

