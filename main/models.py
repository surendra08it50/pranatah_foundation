from django.db import models

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
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.name