from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("causes/", views.causes, name="causes"),
    path("donate/", views.donate, name="donate"),
    path("blog/", views.blog, name="blog"),
    path("gallery/", views.gallery, name="gallery"),
    path("event/", views.event, name="event"),
    path("contact/", views.contact, name="contact"),
    path("blog-single/", views.blog_single, name="blog_single"),
]
