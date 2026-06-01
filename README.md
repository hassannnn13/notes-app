# Flask Notes App

A simple Notes Management application built with Flask and SQLAlchemy. Users can create, view, edit, delete, pin, and search notes through a clean web interface.

## Features

### CRUD Operations

* Create new notes
* View all notes
* Edit existing notes
* Delete notes

### Additional Features

* Search notes by keyword
* Categories for organization
* Pin important notes
* Automatic creation timestamps
* SQLite database storage
* Responsive card-based UI

## Technologies Used

* Python
* Flask
* SQLAlchemy
* SQLite
* HTML5
* CSS3
* Jinja2

## Project Structure

notes-app/
├── app.py
├── notes.db
├── requirements.txt
├── README.md
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   └── edit.html
└── instance/

## Installation

### Clone Repository

git clone <repository-url>

### Navigate to Project

cd notes-app

### Create Virtual Environment

python -m venv venv

### Install Dependencies

pip install -r requirements.txt

### Run Application

python app.py

### Open Browser

http://127.0.0.1:5000

## Author

Hassan Idrees
