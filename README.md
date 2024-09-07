# CI3 Flask Books Application

Link to live project: [CI3 Flask Books](https://github.com/bizboz1981/CI3-flask-books)

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
This project is a Flask-based book management system. The motivation behind this project was to provide a user-friendly application for managing books, tracking authors, and maintaining user records. It aims to merge the power of Flask as a Python micro-framework with a clean and intuitive frontend, making book management simple and efficient. By leveraging RESTful API architecture and database interactions, the application demonstrates the ease of CRUD (Create, Read, Update, Delete) operations with Flask.

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
- Add user profiles for personal book collections.
- Integrate a review system where users can rate and review books.
- Implement borrowing/loan tracking.
- Add email notifications for book updates or new entries.

## Design
### Wireframes
The wireframes are designed to be simple, with a focus on usability. The layout is clean, ensuring users can easily navigate and manage entries.

### Colour Scheme
The application uses neutral colors, such as blues and greys, to maintain a professional and functional appearance, without unnecessary distractions.

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
- SQLite - The database system used.
- Bootstrap - For responsive and mobile-friendly design.

### Other Tech & VS Code Extensions
- [Flask Debug Toolbar](https://flask-debugtoolbar.readthedocs.io/) - for debugging and testing.
- [Postman](https://www.postman.com/) - for API testing.
- [Prettier](https://prettier.io) - for code formatting.

### Learning Resources
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/) - for backend guidance.
- [W3Schools](https://www.w3schools.com) - for frontend and design inspiration.
- [Stack Overflow](https://stackoverflow.com) - for troubleshooting issues.

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

### Steps to Deploy:
1. Fork the repository from [GitHub](https://github.com/bizboz1981/CI3-flask-books).
2. Clone the repository to your local machine: 

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**June 18, 2024,** Add Mongo back into template

**June 14, 2024,** Temporarily remove Mongo until the key issue is resolved

**May 28 2024:** Fix Mongo and Links installs

**April 26 2024:** Update node version to 16

**September 20 2023:** Update Python version to 3.9.17.

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
