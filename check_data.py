from models import db, User, Book, Review, Category
from app import app  # Replace 'your_flask_app' with the actual name of your Flask app module

def check_data_population():
    with app.app_context():
        users = User.query.all()
        books = Book.query.all()
        reviews = Review.query.all()
        categories = Category.query.all()

        print(f"Users: {len(users)}")
        print(f"Books: {len(books)}")
        print(f"Reviews: {len(reviews)}")
        print(f"Categories: {len(categories)}")

if __name__ == "__main__":
    check_data_population()
    
def insert_sample_data():
    user = User(username='testuser', email='test@example.com', password_hash='hashed_password')
    db.session.add(user)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        insert_sample_data()