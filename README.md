# delete_django_table
How to delete a single table in Django 4.0

1. Remove \<DeleteThisTable\> model from models.py file
2. Remove \<DeleteThisTable\> from admin.py file and **ALL** other instances of wherever this class is used.
3. python manage.py makemigrations shapes
4. python manage.py migrate

## `main` Branch

This branch serves as a base to test out deletion methods.

## `try-remove-class` Branch

This branch serves as an example of a successful deletion of the intended table.

## `try-orm-drop` Branch

A failed method of dropping a table in Django 4.0.

## `notes.txt`

Step-by-step how I set up this project and what methods I used.
