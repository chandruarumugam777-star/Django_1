from django.contrib import admin

# Register your models here.
from .models import Book  # Import your Book model

# Register the model so it appears in admin
admin.site.register(Book)