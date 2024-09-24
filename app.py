import os
import base64
from extensions import db, migrate
from models import Book, Review, Category, User, ContactMessage, ReadingList
from forms import RegistrationForm, LoginForm, ReviewForm, BookForm, ContactForm, UpdateBookDetailsForm, EditProfileForm
from datetime import datetime, timezone
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from flask import Flask, render_template, abort, redirect, url_for, flash, request # type: ignore
from functools import wraps
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file


# Create the Flask application instance
def create_app():
    # Initialize the Flask application
    app = Flask(__name__, static_folder='static')


    # Configuration for PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://u44rtq8lrlnr5l:pfa61c23e415abe4f10260bab560e9c7f762ba7fc9fde2c68757f92940a0b6f20@c7u1tn6bvvsodf.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d7q5q599jdl134"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


    # Initialize the database
    db.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate


    # define admin class    
    class ReviewAdmin(ModelView):
        column_list = ('review_id', 'book_title', 'user_id', 'rating', 'review_text', 'created_at')


    # Initialize Flask-Admin
    admin = Admin(app, name='Admin Portal', template_mode='bootstrap3')
    admin.add_view(ReviewAdmin(Review, db.session, name='ReviewAdmin'))


    # Protect the admin portal
    class AdminModelView(ModelView):
        def is_accessible(self):
            return current_user.is_authenticated and current_user.role == 'admin'


    # Add models to the admin interface
    admin.add_view(AdminModelView(Book, db.session, name='BookAdmin'))
    admin.add_view(AdminModelView(User, db.session, name='UserAdmin'))
    admin.add_view(AdminModelView(Category, db.session, name='CategoryAdmin'))
    admin.add_view(AdminModelView(ContactMessage, db.session, name='ContactMessageAdmin'))


    # Base64 encode filter for templates
    @app.template_filter('b64encode')
    def b64encode_filter(data):
        return base64.b64encode(data).decode('utf-8')


    # Decorator to ensure the user is an admin
    def admin_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Check if the user is authenticated and has an admin role
            if not current_user.is_authenticated or current_user.role != 'admin':
                abort(403)  # Return a 403 Forbidden error if not an admin
            return f(*args, **kwargs)
        return decorated_function


    # route for home page (index.html)
    @app.route('/')
    def home():
        # Get the search query from the request arguments, default to an empty string if not provided
        query = request.args.get('q', '')
        
        # If a search query is provided, filter books by title or author matching the query
        if query:
            all_books = Book.query.filter(
                (Book.title.ilike(f'%{query}%')) | 
                (Book.author.ilike(f'%{query}%'))
            ).all()
        else:
            # If no search query is provided, retrieve all books
            all_books = Book.query.all()
        
        # Render the index.html template with the list of books
        return render_template('index.html', books=all_books)


    # route for about page
    @app.route('/about')
    def about():
        return render_template('about.html')


    @app.route('/book/<int:book_id>', methods=['GET', 'POST'])
    def book_detail(book_id):
        # Retrieve the book by ID or return a 404 error if not found
        book = Book.query.get_or_404(book_id)
        
        # Create an instance of the ReviewForm
        form = ReviewForm()
        
        # Check if the form is submitted and the user is authenticated
        if form.validate_on_submit() and current_user.is_authenticated:
            # Create a new review object with the form data
            review = Review(
                rating=form.rating.data,
                review_text=form.review_text.data,
                book_id=book.book_id,
                user_id=current_user.user_id
            )
            # Add the review to the database session and commit
            db.session.add(review)
            db.session.commit()
            
            # Flash a success message and redirect to the book detail page
            flash('Your review has been added.')
            return redirect(url_for('book_detail', book_id=book.book_id))
        
        # Render the book_detail.html template with the book and form
        return render_template('book_detail.html', book=book, form=form)


    @app.route('/register', methods=['GET', 'POST'])
    def register():
        # Create an instance of the RegistrationForm
        form = RegistrationForm()
        
        # Check if the form is submitted and validated
        if form.validate_on_submit():
            # Create a new user object with the form data
            user = User(
                username=form.username.data,
                email=form.email.data,
                profile_picture_url=form.profile_picture_url.data,
                created_at=datetime.now(timezone.utc),
                role='admin' if form.email.data.endswith('@admin.com') else 'regular'  # Assign role based on email domain
            )
            # Set the user's password
            user.set_password(form.password.data)
            
            # Add the user to the database session and commit
            db.session.add(user)
            db.session.commit()
            
            # Redirect to the home page after successful registration
            return redirect(url_for('home'))
        
        # Render the register.html template with the form
        return render_template('register.html', title='Register', form=form)


    # profile route
    @app.route('/profile', methods=['GET', 'POST'])
    @login_required
    def profile():
        form = EditProfileForm()
        
        if form.validate_on_submit():
            current_user.username = form.username.data
            current_user.email = form.email.data
            current_user.profile_picture_url = form.profile_picture_url.data
            db.session.commit()
            flash('Your profile has been updated!', 'success')
            return redirect(url_for('profile'))
        
        elif request.method == 'GET':
            form.username.data = current_user.username
            form.email.data = current_user.email
            form.profile_picture_url.data = current_user.profile_picture_url
        
        edit_mode = request.args.get('edit', 'false').lower() == 'true'
        return render_template('profile.html', form=form, user=current_user, edit_mode=edit_mode)

    
    # route for deleting a profile picture
    @app.route('/delete_profile_picture', methods=['POST'])
    @login_required
    def delete_profile_picture():
        # Check if the form method is DELETE
        if request.form.get('_method') == 'DELETE':
            # Set the current user's profile picture URL to None
            current_user.profile_picture_url = None
            # Commit the changes to the database
            db.session.commit()
            # Flash a success message
            flash('Your profile picture has been deleted!', 'success')
        # Redirect to the profile page
        return redirect(url_for('profile'))
    
    
    @app.route('/add_to_reading_list/<int:book_id>', methods=['POST'])
    @login_required
    def add_to_reading_list(book_id):
        book = Book.query.get_or_404(book_id)
        if not any(rl.book_id == book_id for rl in current_user.reading_list):
            new_entry = ReadingList(user_id=current_user.user_id, book_id=book_id)
            db.session.add(new_entry)
            db.session.commit()
            flash('Book added to your reading list!', 'success')
        else:
            flash('Book is already in your reading list.', 'info')
        return redirect(url_for('book_detail', book_id=book_id))

    # Initialize the LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)


    # Define the user loader function for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        # Retrieve the user by ID from the database
        return User.query.get(int(user_id))


    # login route
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        # If the user is already authenticated, redirect to the home page
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        
        # Create an instance of the LoginForm
        form = LoginForm()
        
        # Check if the form is submitted and validated
        if form.validate_on_submit():
            # Retrieve the user by email from the database
            user = User.query.filter_by(email=form.email.data).first()
            
            # If the user does not exist or the password is incorrect, flash an error message
            if user is None or not user.check_password(form.password.data):
                flash('Invalid email or password')
                return redirect(url_for('login'))
            
            # Log in the user and remember the session if requested
            login_user(user, remember=form.remember_me.data)
            
            # Redirect to the home page after successful login
            return redirect(url_for('home'))
        
        # Render the login.html template with the form
        return render_template('login.html', title='Login', form=form)


    # logout route
    @app.route('/logout')
    def logout():
        # Log out the current user
        logout_user()
        # Redirect to the home page after logging out
        return redirect(url_for('home'))

    # Context processor to inject the current year into all templates
    @app.context_processor
    def inject_current_year():
        # Return a dictionary with the current year
        return {'current_year': datetime.now().year}


    # route for adding a review
    @app.route('/book/<int:book_id>/review', methods=['GET', 'POST'])
    @login_required
    def add_review(book_id):
        # Create an instance of the ReviewForm
        form = ReviewForm()
        
        # Retrieve the book by ID or return a 404 error if not found
        book = Book.query.get_or_404(book_id)
        
        # Check if the form is submitted and the user is authenticated
        if form.validate_on_submit():
            # Create a new review object with the form data
            review = Review(
                rating=form.rating.data,
                review_text=form.review_text.data,
                book_id=book.id,
                user_id=current_user.id
            )
            # Add the review to the database session and commit
            db.session.add(review)
            db.session.commit()
            
            # Flash a success message and redirect to the book detail page
            flash('Your review has been added.')
            return redirect(url_for('book_detail', book_id=book.id))
        
        # Render the add_review.html template with the form and book
        return render_template('add_review.html', form=form, book=book)


    # route for adding a book
    @app.route('/add_book', methods=['GET', 'POST'])
    def add_book():
        form = BookForm()
        if form.validate_on_submit():
            # Check if a book with the same ISBN already exists
            existing_book = Book.query.filter_by(isbn=form.isbn.data).first()
            if existing_book:
                flash('A book with this ISBN already exists.', 'danger')
                return redirect(url_for('add_book'))
            
            # Create a new book instance
            new_book = Book(
                title=form.title.data,
                author=form.author.data,
                published_date=form.published_date.data,
                isbn=form.isbn.data,
                summary=form.summary.data,
                cover_image_url=form.cover_image_url.data,
                created_at=datetime.utcnow()
            )

            # Add the new book to the database
            db.session.add(new_book)
            db.session.commit()

            # Flash a success message and redirect to the book detail page
            flash('Book added successfully!', 'success')
            return redirect(url_for('book_detail', book_id=new_book.book_id))

        return render_template('add_book.html', form=form)


    # route for updating a book description
    @app.route('/book/<int:book_id>/update', methods=['GET', 'POST'])
    @login_required
    def update_book_details(book_id):
        # Retrieve the book by ID or return a 404 error if not found
        book = Book.query.get_or_404(book_id)
        
        # Create an instance of the UpdateBookDescriptionForm
        form = UpdateBookDetailsForm()

        # Check if the form is submitted and validated
        if form.validate_on_submit():
            # Update the book's summary with the new description from the form
            book.title = form.title.data
            book.author = form.author.data
            book.cover_image_url = form.cover_image_url.data
            book.summary = form.description.data
            book.published_date = form.published_date.data
            book.categories = [Category.query.get(category_id) for category_id in form.categories.data]
            # Commit the changes to the database
            db.session.commit()
            # Flash a success message and redirect to the book detail page
            flash('Book details updated successfully!', 'success')
            return redirect(url_for('book_detail', book_id=book_id))

        # Pre-populate the form with the existing description if the request method is GET
        if request.method == 'GET':
            form.title.data = book.title
            form.author.data = book.author
            form.cover_image_url.data = book.cover_image_url
            form.description.data = book.summary
            form.published_date.data = book.published_date
            form.categories.data = [category.category_id for category in book.categories]
        
        # Render the update_book_details.html template with the form and book
        return render_template('update_book_details.html', form=form, book=book)


    # route for submitting a contact form message
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        form = ContactForm()
        if form.validate_on_submit():
            new_message = ContactMessage(
                name=form.name.data,
                email=form.email.data,
                message=form.message.data
            )
            db.session.add(new_message)
            db.session.commit()
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))
        return render_template('contact.html', form=form)
    
    
    # Define the custom 404 error handler
    def page_not_found(e):
        return render_template('404.html'), 404
    
    
    # Define the custom 401 error handler
    def unauthorized(e):
        return render_template('401.html'), 401
    
    
    # Register the custom 404 error handler
    app.register_error_handler(401, unauthorized)
    app.register_error_handler(404, page_not_found)


    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
    
    
    @app.errorhandler(401)
    def unauthorized(e):
        return render_template('401.html'), 401
    
    
    return app





if __name__ == '__main__':
    # Create the Flask application instance
    app = create_app()
    
    # Run the Flask development server
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),  # Get the IP address from environment variables or default to 0.0.0.0
        port=int(os.environ.get("PORT", 8080)),  # Get the port from environment variables or default to 8080
        debug=True  # Enable debug mode for development
    )