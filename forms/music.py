from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class MusicForm(FlaskForm):
    playlist = StringField('Плейлист', validators=[DataRequired()])
    number_of_files = IntegerField('Количество файлов', validators=[DataRequired()])
    executor = StringField('Исполнитель', validators=[DataRequired()])
    start_date = StringField('Start date')
    end_date = StringField('End date')
    is_finished = BooleanField("Is finished")
    submit = SubmitField('Submit')