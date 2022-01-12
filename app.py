import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))


@app.route('/')
def index():
    # show all items
    item_list = Item.query.order_by(Item.id)
    return render_template('base.html', item_list=item_list)


@app.route('/add', methods=["POST"])
def add():
    # add new item
    title = request.form.get("title")
    new_item = Item(title=title)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:item_id>")
def delete(item_id):
    # delete item
    item = Item.query.filter_by(id=item_id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("index"))