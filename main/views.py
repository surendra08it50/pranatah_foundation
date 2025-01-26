from django.shortcuts import render, redirect
from .models import Cause, ContactMessage
from django.contrib import messages
from .forms import VolunteerForm
from .models import Volunteer  # Import Volunteer model

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

def volunteer_register(request):
    return render(request, "volunteer_register.html")

def causes(request):
    causes = Cause.objects.all()
    return render(request, 'causes.html', {'causes': causes})

def volunteer_list(request):
    volunteers = Volunteer.objects.all()  # Fetch all volunteers from the database
    return render(request, "volunteer_list.html", {"volunteers": volunteers})


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
            messages.success(request, 'You have successfully registered as a volunteer!')
            return redirect("volunteer_register")  # Redirect to a success page
        else:
            print(form.errors)
            messages.error(request, 'There was an error with your registration. Please try again.')
    else:
        form = VolunteerForm()
    return render(request, "volunteer_register.html", {"form": form})


def volunteer_success(request):
    return render(request, "volunteer_success.html")



