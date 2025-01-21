from django.shortcuts import render, redirect
from .models import Donor
from django.contrib import messages

def donate(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        amount = request.POST['amount']
        Donor.objects.create(name=name, email=email, amount=amount)
        messages.success(request, "Thank you for your donation!")
        return redirect('home')
    return render(request, 'donate.html')
