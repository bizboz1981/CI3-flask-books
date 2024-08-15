import os
from app import app, db
from models import Category

# Ensure the instance path is set correctly
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'books.db')

# List of categories to add
categories = [
    "Fiction",
    "Classics",
    "Historical",
    "Dystopian",
    "Romance",
    "Adventure",
    "Young Adult",
    "Psychological",
    "Philosophical",
    "Modernist",
    "Epic",
    "Horror",
    "Tragedy",
    "Poetry",
    "Magical Realism",
    "Satire",
    "War",
    "Gothic",
    "Fantasy",
    "Children"
]

# Push an application context
with app.app_context():
    # Add categories to the database
    for category_name in categories:
        # Check if the category already exists
        existing_category = Category.query.filter_by(category_name=category_name).first()
        if not existing_category:
            category = Category(category_name=category_name)
            db.session.add(category)

    db.session.commit()
    print("Categories added successfully!")