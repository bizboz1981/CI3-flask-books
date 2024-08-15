from app import app, db
from models import BookCategory

with app.app_context():
    book_categories = BookCategory.query.all()
    for bc in book_categories:
        print(f'Book ID: {bc.book_id}, Category ID: {bc.category_id}')