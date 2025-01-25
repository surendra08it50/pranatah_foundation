from django.shortcuts import render, redirect
from .models import Cause, ContactMessage
from django.contrib import messages
from .forms import VolunteerForm

def home(request):
    causes = Cause.objects.all()
    return render(request, 'index.html', {'causes': causes})

def about(request):
    return render(request, 'about.html')

def donate(request):
    return render(request, 'donate.html')

def blog(request):
    return render(request, 'blog.html')

def gallery(request):
    return render(request, 'gallery.html')

def event(request):
    return render(request, 'event.html')

def blog_single(request):
    return render(request, "blog-single.html")

def causes(request):
    causes = Cause.objects.all()
    return render(request, 'causes.html', {'causes': causes})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, "Message sent successfully!")
        return redirect("contact")

    return render(request, 'contact.html')



def volunteer_view(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("volunteer_success")  # Redirect to a success page
    else:
        form = VolunteerForm()
    return render(request, "volunteer.html", {"form": form})


def volunteer_success(request):
    return render(request, "volunteer_success.html")