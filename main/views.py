from django.shortcuts import render, redirect
from .models import Cause, ContactMessage
from django.contrib import messages
from .forms import VolunteerForm
from .models import Volunteer, Donation  # Import Volunteer model
from django.core.paginator import Paginator

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
    # volunteers = Volunteer.objects.all()  # Fetch all volunteers from the database
    # return render(request, "volunteer_list.html", {"volunteers": volunteers})
    volunteers = Volunteer.objects.all()  # Get all volunteers
    paginator = Paginator(volunteers, 2)  # Show 5 volunteers per page

    page_number = request.GET.get('page')  # Get page number from URL
    page_obj = paginator.get_page(page_number)  # Get the page object

    return render(request, 'volunteer_list.html', {'page_obj': page_obj})


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



def donate_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        amount = request.POST.get("amount")

        # Save to database
        Donation.objects.create(name=name, email=email, amount=amount)
        return redirect("donate")

    # Fetch all donations with pagination (6 per page)
    donations = Donation.objects.all().order_by("-id")  
    paginator = Paginator(donations, 2)  
    page_number = request.GET.get("page")
    donors = paginator.get_page(page_number)

    return render(request, "donate.html", {"donors": donors})