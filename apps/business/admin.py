from django.contrib import admin
from .models import Barangay, Business, Category

admin.site.register(Business)
admin.site.register(Category)
admin.site.register(Barangay)