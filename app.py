from flask import Flask, render_template, request # type: ignore
import os
from extensions import db, migrate
from models import Book, Review, Category, BookCategory, ReviewVote, User, Authentication
from forms import RegistrationForm
import secrets

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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/books')
def books():
    all_books = Book.query.all()
    return render_template('books.html', books=all_books)

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_detail.html', book=book)

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
            password_hash=form.password.data, 
            profile_picture_url=form.profile_picture_url.data,
            created_at=datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
        # Redirect to a different page after successful registration
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", 8080)),
        debug=True)