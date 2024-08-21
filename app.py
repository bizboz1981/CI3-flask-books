import os
from extensions import db, migrate
from models import Book, Review, Category, BookCategory, User
from forms import RegistrationForm, LoginForm, ReviewForm, BookForm
from datetime import datetime, timezone
from flask_login import login_user, logout_user, current_user, login_required, LoginManager
from flask import Flask, render_template, abort, redirect, url_for, flash # type: ignore
from functools import wraps
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

def create_app():
    app = Flask(__name__)

    # Configuration for SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'books.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Generate a secret key
    secret_key = '+$2At1z~QE7_^7il`'
    app.config['SECRET_KEY'] = secret_key

    # Initialize the database
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize Flask-Admin
    admin = Admin(app, name='Admin Portal', template_mode='bootstrap3')

    # Protect the admin portal
    class AdminModelView(ModelView):
        def is_accessible(self):
            return current_user.is_authenticated and current_user.role == 'admin'

    # Add models to the admin interface
    admin.add_view(AdminModelView(Book, db.session))
    admin.add_view(AdminModelView(Review, db.session))
    admin.add_view(AdminModelView(User, db.session))
    admin.add_view(AdminModelView(Category, db.session))


    def admin_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != 'admin':
                abort(403)
            return f(*args, **kwargs)
        return decorated_function

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/bootstrap')
    @admin_required
    def bootstrap():
        return render_template('bootstrap.html')

    @app.route('/books')
    def books():
        all_books = Book.query.all()
        return render_template('books.html', books=all_books)

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

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

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
            
            published_date_str = form.published_date.data
            published_date = datetime.strptime(published_date_str, '%d/%m/%Y').date()
            
            book = Book(
                title=form.title.data,
                author=form.author.data,
                published_date=published_date,
                isbn=form.isbn.data,
                summary=form.summary.data,
                cover_image_url=form.cover_image_url.data
            )
            db.session.add(book)
            db.session.commit()

            for category_id in form.categories.data:
                book_category = BookCategory(book_id=book.book_id, category_id=category_id)
                db.session.add(book_category)
            
            db.session.commit()
            flash('Book added successfully!', 'success')
            return redirect(url_for('add_book'))
        
        return render_template('add_book.html', form=form)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 8080)),
        debug=True
    )