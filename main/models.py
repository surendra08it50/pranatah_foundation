from django.db import models
from django.utils.timezone import now
class Cause(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="causes/")

    def __str__(self):
        return self.title

class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - ${self.amount}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.name}"

class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10)  # Mobile number (mandatory)
    email = models.EmailField(blank=True, null=True)  # Make email optional
    message = models.TextField()

    def __str__(self):
        return self.name

class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)  # Ensure this line exists

    def __str__(self):
        return f"{self.name} donated ${self.amount}"