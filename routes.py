from flask import Blueprint, request, redirect, url_for, render_template
from models import Item, db


main = Blueprint('main', __name__)


@main.route('/')
def index():
    # show all items
    item_list = Item.query.all()
    return render_template('home_page.html', item_list=item_list)


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


@main.route("/edit_form/<int:item_id>")
def edit_form(item_id):
    # redirect to edit page
    item = Item.query.filter(Item.id == item_id).first()
    return render_template('edit_form_page.html', edit_item=item)


@main.route("/submit_edit", methods=["POST"])
def submit_edit():
    item_id = request.form.get("id")
    title = request.form.get("title")
    description = request.form.get("description")

    Item.query.filter(Item.id == item_id).update({"title": title})
    Item.query.filter(Item.id == item_id).update({"description": description})

    db.session.commit()
    return redirect(url_for("main.index"))


