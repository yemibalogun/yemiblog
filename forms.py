from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
    

class RegisterForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(message='Field Required')])
    password = PasswordField('Password', [validators.DataRequired(message='Field Required')])
    name = StringField('Name', [validators.DataRequired(message='Field Required')])
    submit = SubmitField("Sign Me Up!")
    
class LoginForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(message='Field Required')])
    password = PasswordField('Password', [validators.DataRequired(message='Field Required')])
    submit = SubmitField("Login")
    
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
