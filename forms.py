from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, URLField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Optional, URL
from wtforms import BooleanField, IntegerField, DateField, NumberRange, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    profile_picture_url = URLField('Profile Picture URL', validators=[Optional(), URL()])
    submit = SubmitField('Sign Up')
    
class ReviewForm(FlaskForm):
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    review_text = TextAreaField('Review', validators=[Optional()])
    submit = SubmitField('Submit Review')

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    published_date = DateField('Published Date', validators=[Optional()])
    isbn = StringField('ISBN', validators=[Optional(), Length(max=13)])
    summary = TextAreaField('Summary', validators=[Optional()])
    cover_image_url = StringField('Cover Image URL', validators=[Optional(), Length(max=255)])
    submit = SubmitField('Add Book')