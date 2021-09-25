from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Who are You?.',validators = [Required()])
    submit = SubmitField('submit')