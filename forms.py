from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    URLField,
    TextAreaField,
    SelectMultipleField,
    widgets,
    HiddenField,
    BooleanField,
    DateField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Optional,
    URL,
    Length,
    ValidationError,
)

from models import Category


# Form for user login
class LoginForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email()]
    )  # Email field with required and email format validators
    password = PasswordField(
        "Password", validators=[DataRequired()]
    )  # Password field with required validator
    remember_me = BooleanField("Remember Me")  # Checkbox to remember the user
    submit = SubmitField("Login")  # Submit button


# Form for user registration
class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired()]
    )  # Username field with required validator
    email = StringField(
        "Email", validators=[DataRequired(), Email()]
    )  # Email field with required and email format validators
    password = PasswordField(
        "Password", validators=[DataRequired()]
    )  # Password field with required validator
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )  # Confirm password field with required and equality validators
    profile_picture_url = URLField(
        "Profile Picture URL", validators=[Optional(), URL()]
    )  # Optional URL field for profile picture
    submit = SubmitField("Sign Up")  # Submit button


# Form for submitting a review
class ReviewForm(FlaskForm):
    rating = HiddenField(
        "Rating", validators=[DataRequired()]
    )  # Hidden field for rating with required validator
    review_text = TextAreaField(
        "Review", validators=[DataRequired()]
    )  # Text area for review text with required validator
    submit = SubmitField("Submit Review")  # Submit button

    # Custom validator for rating field
    def validate_rating(self, field):
        try:
            field.data = int(field.data)  # Convert rating to integer
        except ValueError:
            raise ValidationError(
                "Rating must be an integer."
            )  # Raise error if conversion fails
        if not (1 <= field.data <= 5):
            raise ValidationError(
                "Rating must be between 1 and 5."
            )  # Raise error if rating is not between 1 and 5


# Form for adding a book
class BookForm(FlaskForm):
    title = StringField(
        "Title", validators=[DataRequired()]
    )  # Title field with required validator
    author = StringField(
        "Author", validators=[DataRequired()]
    )  # Author field with required validator
    published_date = DateField(
        "Published Date", validators=[DataRequired()]
    )  # Date field for published date with required validator
    isbn = StringField(
        "ISBN", validators=[Optional(), Length(min=10, max=13)]
    )  # Optional ISBN field with length validator
    summary = StringField(
        "Summary", validators=[DataRequired()]
    )  # Summary field with required validator
    cover_image_url = StringField("Cover Image URL")  # Field for cover URL

    # Multiple select field for categories with checkboxes
    categories = SelectMultipleField(
        "Categories", coerce=int, option_widget=widgets.CheckboxInput()
    )

    submit = SubmitField("Add Book")  # Submit button

    # Initialize form with category choices from the database
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.categories.choices = [
            (category.category_id, category.category_name)
            for category in Category.query.all()
        ]


# Form for updating book details
class UpdateBookDetailsForm(FlaskForm):
    title = StringField(
        "Title", validators=[DataRequired()]
    )  # Title field with required validator
    author = StringField(
        "Author", validators=[DataRequired()]
    )  # Author field with required validator
    cover_image_url = StringField(
        "Cover Image URL", validators=[Optional(), URL()]
    )  # Optional URL field for cover image with URL validator
    description = TextAreaField(
        "Description", validators=[DataRequired()]
    )  # Text area for description with required validator
    published_date = DateField(
        "Published Date", validators=[DataRequired()]
    )  # Date field for published date with required validator
    categories = SelectMultipleField(
        "Categories", coerce=int, option_widget=widgets.CheckboxInput()
    )  # Multiple select field for categories with checkboxes
    submit = SubmitField("Update Book Details")  # Submit button

    # Initialize form with category choices from the database
    def __init__(self, *args, **kwargs):
        super(UpdateBookDetailsForm, self).__init__(*args, **kwargs)
        self.categories.choices = [
            (category.category_id, category.category_name)
            for category in Category.query.all()
        ]


# Form for contacting
class ContactForm(FlaskForm):
    name = StringField(
        "Name", validators=[DataRequired()]
    )  # Name field with required validator
    email = StringField(
        "Email", validators=[DataRequired(), Email()]
    )  # Email field with required and email format validators
    message = TextAreaField(
        "Message", validators=[DataRequired()]
    )  # Text area for message with required validator
    submit = SubmitField("Send Message")  # Submit button


# Form for editing user profile
class EditProfileForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired()]
    )  # Username field with required validator
    email = StringField(
        "Email", validators=[DataRequired(), Email()]
    )  # Email field with required and email format validators
    profile_picture_url = URLField(
        "Profile Picture URL", validators=[Optional(), URL()]
    )  # Optional URL field for profile picture with URL validator
    submit = SubmitField("Update Profile")  # Submit button
