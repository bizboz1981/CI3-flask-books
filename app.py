import os
import base64
from extensions import db, migrate
from models import Book, Review, Category, User, ContactMessage
from forms import RegistrationForm, LoginForm, ReviewForm, BookForm, ContactForm
from datetime import datetime, timezone
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from flask import Flask, render_template, abort, redirect, url_for, flash, request # type: ignore
from functools import wraps
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from dotenv import load_dotenv
from flask_mail import Mail, Message

load_dotenv()  # Load environment variables from .env file

def create_app():
    app = Flask(__name__, static_folder='static')

    # Configuration for SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'books.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # get secret key
    app.config['SECRET_KEY'] = "+$2At1z~QE7_^7il`"

    # Initialize the database
    db.init_app(app)
    migrate.init_app(app, db)
    
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

    @app.template_filter('b64encode')
    def b64encode_filter(data):
        return base64.b64encode(data).decode('utf-8')

    def admin_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != 'admin':
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    
    # # Configure Flask-Mail
    # app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    # app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
    # app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
    # app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    # app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

    # mail = Mail(app)

    @app.route('/')
    def home():
        query = request.args.get('q', '')
        if query:
            all_books = Book.query.filter(
                (Book.title.ilike(f'%{query}%')) | 
                (Book.author.ilike(f'%{query}%'))
            ).all()
        else:
            all_books = Book.query.all()
        return render_template('index.html', books=all_books)

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/bootstrap')
    @admin_required
    def bootstrap():
        return render_template('bootstrap.html')


    @app.route('/book/<int:book_id>', methods=['GET', 'POST'])
    def book_detail(book_id):
        book = Book.query.get_or_404(book_id)
        form = ReviewForm()
        if form.validate_on_submit() and current_user.is_authenticated:
            review = Review(
                rating=form.rating.data,
                review_text=form.review_text.data,
                book_id=book.book_id,
                user_id=current_user.user_id
            )
            db.session.add(review)
            db.session.commit()
            flash('Your review has been added.')
            return redirect(url_for('book_detail', book_id=book.book_id))
        return render_template('book_detail.html', book=book, form=form)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(
                username=form.username.data,
                email=form.email.data,
                profile_picture_url=form.profile_picture_url.data,
                created_at=datetime.now(timezone.utc),
                role='admin' if form.email.data.endswith('@admin.com') else 'regular'
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('register.html', title='Register', form=form)


    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid email or password')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('home'))
        return render_template('login.html', title='Login', form=form)


    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('home'))


    @app.context_processor
    def inject_current_year():
        return {'current_year': datetime.now().year}

    @app.route('/book/<int:book_id>/review', methods=['GET', 'POST'])
    @login_required
    def add_review(book_id):
        form = ReviewForm()
        book = Book.query.get_or_404(book_id)
        if form.validate_on_submit():
            review = Review(
                rating=form.rating.data,
                review_text=form.review_text.data,
                book_id=book.id,
                user_id=current_user.id
            )
            db.session.add(review)
            db.session.commit()
            flash('Your review has been added.')
            return redirect(url_for('book_detail', book_id=book.id))
        return render_template('add_review.html', form=form, book=book)

    @app.route('/add_book', methods=['GET', 'POST'])
    def add_book():
        form = BookForm()
        if form.validate_on_submit():            
            new_book = Book(
                title=form.title.data,
                author=form.author.data,
                isbn=form.isbn.data,
                summary=form.summary.data,
                cover_image_url=form.cover_image_url.data,
            )
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))
        return render_template('add_book.html', form=form)

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
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 8080)),
        debug=True
    )