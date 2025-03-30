# File Manager

A web application built with Django and React for managing user files, profiles, and dashboards. Users can register, log in, upload files, view file lists, and update their profiles with usernames, phone numbers, and multiple addresses. The UI is styled with Tailwind CSS for a modern, user-friendly experience.

## Features

- **User Authentication**: Register, login, and logout functionality.
- **Profile Management**: Edit username, phone number, and manage multiple addresses.
- **File Management**: Upload files, view file list with download links.
- **Dashboard**: View total files, file types, and user file counts.

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Frontend**: React, React Router
- **Database**: SQLite (default, configurable to others)
- **Dependencies**: Axios, Python, Node.js

## Prerequisites

- Python 3.8+ (e.g., Python 3.12)
- Node.js 18+ (includes npm)
- Git (optional, for cloning)

## Setup Instructions

### 1. Clone the Repository (if applicable)

```bash
git clone <repository-url>
cd file_manager

### 2. Install Python Dependencies
pip install django djangorestframework

#### 3.Apply Migrations

python manage.py makemigrations
python manage.py migrate

### 4.Create Superuser (Optional):
python manage.py createsuperuser

5.Build Frontend

cd frontend
npm run build

6. Start Django server
cd ..  # Back to project root
python manage.py runserver


Open http://localhost:8000/ in your browser.

---- Usage ----
Register: Visit /register/ to create an account.
Login: Use /login/ (Django page) to log in.
Profile: Update details at /profile/.
Upload Files: Go to /upload/ to add files.
View Files: See your files at /files/.
Dashboard: Check stats at /dashboard/.
Logout: Use the navbar to log out.

project structure

file_manager/
├── frontend/             # React frontend
│   ├── src/             # React components and index.css
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── package.json
├── files/               # Django app for file management
├── users/               # Django app for user management
│   └── templates/users/ # Login template
├── file_manager/        # Django project settings
└── README.md
```
