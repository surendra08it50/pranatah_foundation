from django.contrib import admin
from .models import Cause, Donation, ContactMessage

admin.site.register(Cause)
admin.site.register(Donation)
admin.site.register(ContactMessage)
