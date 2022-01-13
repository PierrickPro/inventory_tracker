from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))


def init_db(app):
    db.init_app(app)


def create_db(app):
    with app.app_context():
        db.create_all()
