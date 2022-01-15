from flask import Blueprint, request, redirect, url_for, render_template
from wtformsExtension import AddItemForm, EditItemForm, FilterItemsForm
from models import db, Item


main = Blueprint('main', __name__)


@main.route('/')
def index():
    # show all items
    item_list = Item.query.all()
    add_form = AddItemForm()
    filter_form = FilterItemsForm()
    return render_template('pages/home.html', item_list=item_list, add_form=add_form, filter_form=filter_form)


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


@main.route("/edit/<int:item_id>")
def edit(item_id):
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


@main.route('/submit_filter', methods=["POST"])
def submit_filter():
    # show all items filtered
    name_filter = request.form.get("name")
    description_filter = request.form.get("description")
    kind_filter = request.form.get("kind")
    min_count_filter = request.form.get("min_count")
    max_count_filter = request.form.get("max_count")

    item_list = query_filtered_items(name_filter, description_filter, kind_filter, min_count_filter, max_count_filter)

    add_form = AddItemForm()
    filter_form = FilterItemsForm()
    return render_template('pages/home.html', item_list=item_list, add_form=add_form, filter_form=filter_form)


def query_filtered_items(name_filter, description_filter, kind_filter, min_count_filter, max_count_filter):

    item_list = Item.query.filter(Item.name.contains(name_filter), Item.kind.contains(kind_filter),
                                  Item.description.contains(description_filter))

    # only apply min_count_filter if not null
    if min_count_filter:
        item_list = item_list.filter(Item.count >= min_count_filter)

    # only apply max_count_filter if not null
    if max_count_filter:
        item_list = item_list.filter(Item.count <= max_count_filter)

    return item_list
