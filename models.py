from datetime import datetime, timezone

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db


# User class to define 'users' table
class User(UserMixin, db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)  # PK for User table
    username = db.Column(
        db.String(50), nullable=False, unique=True
    )  # Username of the user, must be unique
    email = db.Column(
        db.String(100), nullable=False, unique=True
    )  # Email of the user, must be unique
    password_hash = db.Column(
        db.String(255), nullable=False
    )  # Hashed password of the user
    profile_picture_url = db.Column(
        db.String(255)
    )  # URL to the profile picture of the user
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(timezone.utc)
    )  # Timestamp when the user was created
    role = db.Column(
        db.String(50), nullable=False, default="regular"
    )  # Role of the user, default is 'regular'

    reviews = db.relationship(
        "Review", backref="user", lazy=True
    )  # Relationship to the Review model
    reading_list = db.relationship(
        "ReadingList", backref="user", lazy=True, cascade="all, delete-orphan"
    )  # Relationship to the ReadingList model

    # set the user's password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # check the user's password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # get the user's ID
    def get_id(self):
        return str(self.user_id)


# Book class to define 'books' table
class Book(db.Model):
    __tablename__ = "books"
    book_id = db.Column(db.Integer, primary_key=True)  # PK for the Book table
    title = db.Column(db.String(255), nullable=False)  # Title of the book
    author = db.Column(db.String(255), nullable=False)  # Author of the book
    published_date = db.Column(db.Date)  # Published date of the book
    isbn = db.Column(db.String(13), unique=True)  # ISBN must be unique
    summary = db.Column(db.Text)  # Summary of the book
    cover_image_url = db.Column(db.String(255))  # URL to cover of the book
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow
    )  # Timestamp when the book was created

    reviews = db.relationship(
        "Review", backref="book", lazy=True, cascade="all, delete-orphan"
    )  # Relationship to the Review model
    categories = db.relationship(
        "Category",
        secondary="book_categories",
        backref=db.backref("book_list", lazy="dynamic"),
    )  # Many-to-many relationship to the Category model
    reading_list_entries = db.relationship(
        "ReadingList", backref="book", lazy=True, cascade="all, delete-orphan"
    )  # Relationship to the ReadingList model


# Review class to define 'reviews' table
class Review(db.Model):
    __tablename__ = "reviews"
    review_id = db.Column(
        db.Integer, primary_key=True
    )  # Primary key for the Review table
    book_id = db.Column(
        db.Integer, db.ForeignKey("books.book_id"), nullable=False
    )  # Foreign key to the Book table
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.user_id"), nullable=False
    )  # Foreign key to the User table
    rating = db.Column(db.Integer, nullable=False)  # Rating given by the user
    review_text = db.Column(db.Text)  # Text of the review
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow
    )  # Timestamp when the review was created

    # Returns the title of the book being reviewed
    @property
    def book_title(self):
        return self.book.title if self.book else "N/A"


# Category class to define 'categories' table
class Category(db.Model):
    __tablename__ = "categories"
    category_id = db.Column(
        db.Integer, primary_key=True
    )  # Primary key for the Category table
    category_name = db.Column(
        db.String(50), nullable=False, unique=True
    )  # Name of the category, must be unique

    books = db.relationship(
        "BookCategory", backref="category", lazy=True, viewonly=True
    )  # Relationship to the BookCategory model


# ContactMessage class to define 'contact_messages' table
class ContactMessage(db.Model):
    __tablename__ = "contact_messages"
    id = db.Column(
        db.Integer, primary_key=True
    )  # Primary key for the ContactMessage table
    name = db.Column(
        db.String(100), nullable=False
    )  # Name of the person sending the message
    email = db.Column(
        db.String(100), nullable=False
    )  # Email of the person sending the message
    message = db.Column(db.Text, nullable=False)  # The message content
    timestamp = db.Column(
        db.DateTime, default=db.func.current_timestamp(), nullable=False
    )  # Timestamp when the message was sent, defaults to current time


# ReadingList class to define 'reading_list' table
class ReadingList(db.Model):
    # This table has a compound PK made up of 2 FKs: user_id and book_id
    __tablename__ = "reading_list"
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.user_id"), primary_key=True
    )  # Foreign key to the User table, primary key
    book_id = db.Column(
        db.Integer, db.ForeignKey("books.book_id"), primary_key=True
    )  # Foreign key to the Book table, primary key
    added_at = db.Column(
        db.DateTime, default=datetime.utcnow
    )  # Timestamp when book was added to reading list defaults to current time
