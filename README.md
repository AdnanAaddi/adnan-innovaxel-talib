URL Shortening Service

Overview

This is a simple RESTful API that allows users to shorten long URLs. The API provides endpoints to create, retrieve, update, and delete short URLs. It also tracks the number of times a short URL has been accessed.
Features

Create a new short URL

Retrieve an original URL from a short URL

Update an existing short URL

Delete an existing short URL

Get statistics on the number of times a short URL has been accessed

Tech Stack

Backend: Django REST Framework

Database: SQLite (default) / PostgreSQL / MySQL

Language: Python

Installation

Prerequisites

Python 3.8+

Django 4.0+

Django REST Framework
Setup

Clone the repository:

git clone git@github.com:AdnanAaddi/adnan-innovaxel-talib.git
cd url-shortener

Create and activate a virtual environment:

python -m venv venv
# On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Run database migrations:

python manage.py migrate

Start the development server:

python manage.py runserver

API Endpoints

1. Create Short URL

Endpoint: POST api/shorten/

2. Retrieve Original URL

Endpoint: GET api/shorten/{short_code}/

3. Update Short URL

Endpoint: PUT api/shorten/{short_code}/

4. Delete Short URL

Endpoint: DELETE api/shorten/delete/{short_code}/

5. Get URL Statistics

Endpoint: GET api/shorten/stats/{short_code}/
