# Filesave
## Description

The File Saving App is a simple web application built with Django and SQLite3 that allows users to upload and save files securely. This app provides a convenient way to store and manage files in a database, making it easy to access and download them at any time.

## Features

- User-friendly interface for file uploading and management.
- Files are securely stored in a SQLite3 database.
- Each file entry contains metadata like file name, upload date, etc.
- Download option available for files, making retrieval straightforward.
- Responsive design, compatible with various devices and screen sizes.
  
## How to run this app
1. clone the repository
2. cd filesave
3. python -m venv venv
4.venv\Scripts\activate -for windows
5.source venv/bin/activate -for linux
6.pip install -r requirements.txt
7.python manage.py migrate
8.python manage.py runserver


