
from flask import Blueprint, request, redirect, url_for, render_template
from database import db
from models import Item


main = Blueprint('main', __name__)


@main.route('/')
def index():
    # show all items
    item_list = Item.query.order_by(Item.id)
    return render_template('base.html', item_list=item_list)


@main.route('/add', methods=["POST"])
def add():
    # add new item
    title = request.form.get("title")
    description = request.form.get("description")
    new_item = Item(title=title, description=description)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for("main.index"))


@main.route("/delete/<int:item_id>")
def delete(item_id):
    # delete item
    item = Item.query.filter_by(id=item_id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("main.index"))
