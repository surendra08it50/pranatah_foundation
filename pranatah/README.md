pranatah/
│── main/               # Django App
│   ├── migrations/
│   ├── static/         # Static files (CSS, JS, images)
│   ├── templates/      # HTML templates
│   │   ├── about.html
│   │   ├── {% url 'blog_single' %}
│   │   ├── blog.html
│   │   ├── causes.html
│   │   ├── contact.html
│   │   ├── donate.html
│   │   ├── event.html
│   │   ├── gallery.html
│   │   ├── {% url 'home' %}
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
│── pranatah/           # Django Project Config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
│── .gitignore
│── .env
│── db.sqlite3
│── manage.py


1. pip install -r requirements.txt
2. python manage.py makemigrations
    python manage.py migrate

3. python manage.py createsuperuser
4. python manage.py runserver
5. Open Website
    Go to http://127.0.0.1:8000/ 🎉

see all volunteers
http://127.0.0.1:8000/volunteers/    

