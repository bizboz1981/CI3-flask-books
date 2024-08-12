from app import app, db
from models import Book, Category, BookCategory

# Define associations between books and categories
book_categories = {
    "To Kill a Mockingbird": ["Fiction", "Classics", "Historical"],
    "1984": ["Fiction", "Dystopian", "Classics"],
    "Pride and Prejudice": ["Fiction", "Romance", "Classics"],
    "The Great Gatsby": ["Fiction", "Classics", "Historical"],
    "Moby-Dick": ["Fiction", "Classics", "Adventure"],
    "War and Peace": ["Fiction", "Classics", "Historical"],
    "The Catcher in the Rye": ["Fiction", "Classics", "Young Adult"],
    "The Hobbit": ["Fiction", "Fantasy", "Adventure"],
    "Crime and Punishment": ["Fiction", "Classics", "Psychological"],
    "The Brothers Karamazov": ["Fiction", "Classics", "Philosophical"],
    "Ulysses": ["Fiction", "Classics", "Modernist"],
    "The Odyssey": ["Fiction", "Classics", "Epic"],
    "The Iliad": ["Fiction", "Classics", "Epic"],
    "Brave New World": ["Fiction", "Dystopian", "Classics"],
    "Jane Eyre": ["Fiction", "Romance", "Classics"],
    "Wuthering Heights": ["Fiction", "Romance", "Classics"],
    "Frankenstein": ["Fiction", "Horror", "Classics"],
    "Anna Karenina": ["Fiction", "Classics", "Romance"],
    "Madame Bovary": ["Fiction", "Classics", "Tragedy"],
    "The Divine Comedy": ["Fiction", "Classics", "Epic", "Poetry"],
    "One Hundred Years of Solitude": ["Fiction", "Classics", "Magical Realism"],
    "The Sound and the Fury": ["Fiction", "Classics", "Modernist"],
    "Don Quixote": ["Fiction", "Classics", "Adventure"],
    "In Search of Lost Time": ["Fiction", "Classics", "Modernist"],
    "Great Expectations": ["Fiction", "Classics", "Coming-of-Age"],
    "Catch-22": ["Fiction", "Classics", "Satire", "War"],
    "Lolita": ["Fiction", "Classics", "Psychological"],
    "Beloved": ["Fiction", "Classics", "Historical"],
    "Mrs Dalloway": ["Fiction", "Classics", "Modernist"],
    "Middlemarch": ["Fiction", "Classics", "Historical"],
    "The Count of Monte Cristo": ["Fiction", "Classics", "Adventure"],
    "The Picture of Dorian Gray": ["Fiction", "Classics", "Gothic"],
    "The Stranger": ["Fiction", "Classics", "Philosophical"],
    "Fahrenheit 451": ["Fiction", "Dystopian", "Classics"],
    "Dracula": ["Fiction", "Horror", "Classics"],
    "The Adventures of Huckleberry Finn": ["Fiction", "Classics", "Adventure"],
    "The Sun Also Rises": ["Fiction", "Classics", "Historical"],
    "Heart of Darkness": ["Fiction", "Classics", "Adventure"],
    "The Grapes of Wrath": ["Fiction", "Classics", "Historical"],
    "The Old Man and the Sea": ["Fiction", "Classics", "Adventure"],
    "A Tale of Two Cities": ["Fiction", "Classics", "Historical"],
    "Les Misérables": ["Fiction", "Classics", "Historical"],
    "Gulliver’s Travels": ["Fiction", "Classics", "Fantasy", "Satire"],
    "The Scarlet Letter": ["Fiction", "Classics", "Romance"],
    "Alice's Adventures in Wonderland": ["Fiction", "Classics", "Fantasy", "Children"],
    "To the Lighthouse": ["Fiction", "Classics", "Modernist"],
    "Of Mice and Men": ["Fiction", "Classics", "Historical"],
    "The Lord of the Rings": ["Fiction", "Fantasy", "Epic"],
}

# Push an application context
with app.app_context():
    for book_title, category_names in book_categories.items():
        book = Book.query.filter_by(title=book_title).first()
        if book:
            for category_name in category_names:
                category = Category.query.filter_by(category_name=category_name).first()
                if category:
                    book_category = BookCategory(book_id=book.book_id, category_id=category.category_id)
                    db.session.add(book_category)
    
    db.session.commit()
    print("Books and categories associated successfully!")