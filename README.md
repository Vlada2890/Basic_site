# Basic_site
Django site skeleton
1)Install Django
First, ensure you have Django installed. You can install it using pip:

pip install django

2)Create a Django Project
Create a new Django project using the django-admin command:

django-admin startproject mysite

3)Create a Django Application
Navigate into the project directory and create a new application:

cd mysite

python manage.py startapp myapp

Somewhere in the middle) Create and Apply Migrations
Create and apply the database migrations:

python manage.py makemigrations

python manage.py migrate

End)Run the Development Server
Run the development server to see your site in action:

python manage.py runserver

python manage.py runserver'''
