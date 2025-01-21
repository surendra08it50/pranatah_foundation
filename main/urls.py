from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("donate/", views.donate, name="donate"),
    path("causes/", views.causes, name="causes"),
    path("contact/", views.contact, name="contact"),
]
