from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumField, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumField(min=1, max=99)], default=1)