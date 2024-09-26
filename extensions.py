from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy for database operations
from flask_migrate import Migrate  # Import Migrate for handling database migrations
"""
This module initializes and configures the extensions used in the Flask application.

Extensions:
    db (SQLAlchemy): An instance of SQLAlchemy used for database operations.
    migrate (Migrate): An instance of Migrate used for handling database migrations.

Note:
    This file is kept separate to maintain a clean and modular structure, allowing for easier management and configuration of extensions.
"""


db = SQLAlchemy()  # Initialize SQLAlchemy instance
migrate = Migrate()  # Initialize Migrate instance