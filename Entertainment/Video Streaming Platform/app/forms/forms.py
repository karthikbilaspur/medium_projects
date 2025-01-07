from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired

class VideoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    file = FileField('File', validators=[DataRequired()])
    submit = SubmitField('Upload')