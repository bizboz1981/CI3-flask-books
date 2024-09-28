# CI3 Flask Books Application

Link to live project: [CI3 Flask Books](https://ci3-book-review-d8d5166064da.herokuapp.com)

## Table of Contents
- [Project Background & Summary](#project-background--summary)
- [User Experience (UX)](#user-experience-ux)
- [Features & Structure](#features--structure)
- [Design](#design)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [References & Resources Used](#references--resources-used)

## Project Background & Summary
This project is a Flask-based book management system. The motivation behind this project was to provide a user-friendly application for managing books, tracking authors, and maintaining user records. It aims to merge the power of Flask as a Python micro-framework with a clean and intuitive frontend, making book management simple and efficient. The project does not leverage RESTful API architecture; The application demonstrates the ease of CRUD (Create, Read, Update, Delete) operations with Flask. However, DELETE operations are not supported by HTML directly, so these have to be simulated by using POST. DELETE functionality would only be available in a truly RESTful setup.

The project provides a simple interface where users can view, add, edit, or delete book records and associate them with authors. This is designed to be flexible enough for expansion and suitable for different types of users, from avid readers to book clubs.

## User Experience (UX)
### User Stories
#### First Time Visitor Goals
1. As a First Time Visitor, I want to easily understand the purpose of the application and how to navigate through it.
2. As a First Time Visitor, I want to be able to search for books and see the details.
3. As a First Time Visitor, I want a simple way to add or manage books in the system.

#### Returning Visitor Goals
1. As a Returning Visitor, I want to easily find the books I have previously added.
2. As a Returning Visitor, I want to update or delete records with ease.
3. As a Returning Visitor, I want to stay informed about any new updates to the platform.

#### Frequent Visitor Goals
1. As a Frequent Visitor, I want to see all book records displayed in an organized manner.
2. As a Frequent Visitor, I want to ensure that the system functions smoothly with all its features, including book and author management.
3. As a Frequent Visitor, I want to access the system without any technical errors or bugs.

## Features & Structure
### Existing Features
- **Homepage & Navigation**: The homepage provides users with a clean and simple interface, displaying the list of books and a navigation menu for easy access.
- **Book Listing**: Users can view a list of books with details such as title, author, and published year. Clicking on a book title allows the user to view more detailed information.
- **Add/Edit/Delete Book**: Users can add new books, update the details of a book, or delete a book from the system.
- **Author Management**: Manage author details and associate books with specific authors.
- **User Authentication**: Authentication ensures that only registered users can access full functionality, such as adding or editing book records.
- **Search Functionality**: A search bar allows users to quickly find books by title or author.

### Future Features
- Improve reading list features like removing books, or marking as read.
- Add 'forgotten password' feature
- Add email notifications for book updates or new entries.

## Design
### Wireframes
The wireframes are designed to be simple, with a focus on usability. The layout is clean, ensuring users can easily navigate and manage entries.

### Colour Scheme
The application uses neutral colors, such as off-whites and browns, to maintain a classic and functional appearance, without unnecessary distractions.

## Technologies Used
### Languages
- Python (Flask framework)
- HTML5
- CSS3
- JavaScript (for frontend interactivity)

### Applications
- Git - for version control.
- GitHub - for version control and hosting.
- Visual Studio Code - for developing the project.

### Frameworks, Libraries & Tools
- Flask - The primary backend framework.
- Jinja2 - For templating in HTML.
- SQLite - for development and testing.
- PostgreSQL - for production database system.
- Bootstrap - For responsive and mobile-friendly design.

### Other Tech & VS Code Extensions
- [Flask Debug Toolbar](https://flask-debugtoolbar.readthedocs.io/) - for debugging and testing.
- [Prettier](https://prettier.io) - for code formatting.
- [Github Copilot](https://github.com/features/copilot) for debugging and efficient use of terminal

### Learning Resources
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/) - for backend guidance.
- [W3Schools](https://www.w3schools.com) - for frontend and design inspiration.
- [Stack Overflow](https://stackoverflow.com) - for troubleshooting issues.
- [Codecademy](https://www.codecademy.com) - the course on Flask was invaluable.

## Testing
Extensive manual testing has been carried out to ensure all CRUD operations, form validations, and database interactions work correctly.

### Features Testing
| Feature             | Test Case                               | Outcome                                     |
| ------------------- | --------------------------------------- | ------------------------------------------- |
| Book Search         | Search for a book by title or author    | Search results display correct entries      |
| Add New Book        | Add a new book to the collection        | Book is successfully added and displayed    |
| Edit Book Details   | Edit the details of an existing book    | Updates are saved and reflected immediately |
| Delete Book         | Delete a book from the collection       | Book is successfully deleted                |
| Author Management   | Add or edit an author                   | Author details are saved and associated     |

### Browser Testing
| Browser             | Compatibility | Responsiveness | Issues   |
| ------------------- | ------------- | -------------- | -------- |
| Chrome              | Good          | Good           | None     |
| Firefox             | Good          | Good           | None     |
| Safari              | Good          | Good           | None     |
| Edge                | Good          | Good           | None     |

### Online Validation Services
- **HTML Validator**: Validated with no errors.
- **CSS Validator**: Passed with no significant issues.
- **Flask Debugging**: Used Flask's built-in debugger to resolve any backend issues.

## Deployment
The application is deployed on GitHub Pages for frontend hosting. You can also deploy the Flask backend using Heroku.

Please feel free to clone the project and use it for your own site. In order to do this:

### Cloning the Repo
1. Open your terminal and run the following command to clone the repository:```git clone https://github.com/bizboz1981/CI3-flask-books```
2. cd into the new project directory: ```cd CI3-flask-books```
3. Create and activate a virtual environment: <br>```python3 -m venv venv```<br>```source venv/bin/activate``` (On Windows use `venv\Scripts\activate`)
4. Install the required dependencies from the requirements.txt file: ```pip install -r requirements.txt```
5. Create a .env file in the root directory and add the necessary environment variables: ```touch .env```
6. Add the following lines to the .env file: <br> ```SECRET_KEY=your_secret_key``` <br> ```SQLALCHEMY_DATABASE_URI=your_database_uri```

### Deploy to Heroku
1. Log in to your Heroku account using the Heroku CLI: ```heroku login```
2. Create a new Heroku app: ```heroku create your-app-name```
3. Add the Heroku Postgres add-on to your app: ```heroku addons:create heroku-postgresql:hobby-dev``` (depending on your subscription plan)
4. Set environment variables on Heroku:<br>```heroku config:set SECRET_KEY=your_secret_key```<br>```heroku config:set SQLALCHEMY_DATABASE_URI=your_database_uri```
5. Deploy the application to Heroku: ```git push heroku main```
6. Run the database migrations on Heroku: ```heroku run flask db upgrade```
7. Open the dployed application: ```heroku open```