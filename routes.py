from flask import Blueprint, request, redirect, url_for, render_template
from wtformsExtension import AddItemForm, EditItemForm
from models import Item, db


main = Blueprint('main', __name__)


@main.route('/')
def index():
    # show all items
    item_list = Item.query.all()
    form = AddItemForm()
    return render_template('pages/home.html', item_list=item_list, form=form)


@main.route('/add', methods=["POST"])
def add():
    # add new item
    name = request.form.get("name")
    description = request.form.get("description")
    kind = request.form.get("kind")
    count = request.form.get("count")
    new_item = Item(name=name, description=description, kind=kind, count=count)
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
    form = EditItemForm(obj=item)
    return render_template('pages/edit.html', edit_item=item, form=form)


@main.route("/submit_edit", methods=["POST"])
def submit_edit():
    item_id = request.form.get("id")
    name = request.form.get("name")
    kind = request.form.get("kind")
    description = request.form.get("description")
    count = request.form.get("count")

    Item.query.filter(Item.id == item_id).update(
        {"name": name, "kind": kind, "description": description, "count": count})

    db.session.commit()
    return redirect(url_for("main.index"))
