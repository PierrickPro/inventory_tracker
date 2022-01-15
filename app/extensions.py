from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, HiddenField
from wtforms.validators import InputRequired, Length

# wtForms classes


class AddItemForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(max=100)])
    description = StringField('description', validators=[InputRequired(), Length(max=100)])
    kind = StringField('kind', validators=[InputRequired(), Length(max=100)])
    count = IntegerField('count', validators=[InputRequired()])


class FilterItemsForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    kind = StringField('kind')
    min_count = IntegerField('min_count')
    max_count = IntegerField('max_count')


class EditItemForm(FlaskForm):
    id = HiddenField('id', validators=[InputRequired()])
    name = StringField('name', validators=[InputRequired(), Length(max=100)])
    description = StringField('description', validators=[InputRequired(), Length(max=100)])
    kind = StringField('kind', validators=[InputRequired(), Length(max=100)])
    count = IntegerField('count', validators=[InputRequired()])
