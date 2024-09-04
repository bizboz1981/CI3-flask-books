from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, URLField, TextAreaField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Email, EqualTo, Optional, URL, NumberRange, Length
from wtforms import BooleanField, IntegerField
from models import Category

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
    published_date = StringField('Published Date', validators=[DataRequired()])
    isbn = StringField('ISBN', validators=[Optional(), Length(min=10, max=13)])
    summary = StringField('Summary', validators=[DataRequired()])
    cover_image_url = StringField('Cover Image URL')
    
    categories = SelectMultipleField('Categories', coerce=int, option_widget=widgets.CheckboxInput())
    
    submit = SubmitField('Add Book')

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.categories.choices = [(category.category_id, category.category_name) for category in Category.query.all()]

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')