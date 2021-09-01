from django.contrib import admin
from .models import Barangay, Business, Category, Notification, Payment, BusinessCategory, Period, Qrcode, BusinessPeriod

admin.site.register(Business)
admin.site.register(Category)
admin.site.register(Barangay)
admin.site.register(Payment)
admin.site.register(BusinessCategory)
admin.site.register(Notification)
admin.site.register(Qrcode)
admin.site.register(BusinessPeriod)
admin.site.register(Period)