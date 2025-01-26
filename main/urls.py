from django.urls import path
from . import views
from .views import volunteer_view, volunteer_success, volunteer_list,volunteer_register

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
    path("volunteer/", volunteer_view, name="volunteer_form"),
    path("volunteer/success/", volunteer_success, name="volunteer_success"),
    path("volunteers/", volunteer_list, name="volunteer_list"),
    path("volunteer_register/", volunteer_register, name="volunteer_register"),
]

# urlpatterns += [
#     path("volunteer/success/", volunteer_success, name="volunteer_success"),
# ]