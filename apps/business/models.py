from typing import Tuple
from typing_extensions import TypeGuard
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField
from django.db.models.query import BaseIterable


class Category(models.Model):
    SINGLE = 'SINGLE PROPRIETOR'
    PARTNER = 'PARTNERSHIP'
    CORPORATION = 'CORPORATION'
    COOPERATIVE = 'COOPERATIVE'
    OWNERSHIP = ((SINGLE, 'Single Proprietor'), (PARTNER, 'Partnership'),
                (CORPORATION, 'Corporation'), (COOPERATIVE, 'Cooperative'))
    
    FIRST = 'FIRST NOTICE'
    SECOND = 'SECOND NOTICE'
    FINAL = 'THIRD NOTICE'
    CLOSURE = 'SUBJECT FOR CLOSURE'
    NOTICE_STATUS = ((FIRST,'First Notice'), (SECOND,'Second Notice'), 
            (FINAL, 'Final Notice'), (CLOSURE, 'Subject for closure'))

    ACTIVE1 = 'ACTIVE WITHOUT EXTENSION'
    ACTIVE2 = 'ACTIVE WITH EXTENTION'
    INACTIVE = 'INACTIVE'
    BUSINESS_STATUS = ((ACTIVE1,'Active without extension'), (ACTIVE2,'Active with extension'), 
                    (INACTIVE, 'Inactive'))

    ANNUAL = 'ANNUALLY'
    SEMI = 'SEMI-ANNUAL'
    QUARTERLY = 'QUARTERLY'
    PAYMENT_MODE = ((ANNUAL, 'Annually'), (SEMI, 'Semi-annual'), (QUARTERLY, 'Quarterly'))

    TEMPORARY = 'TEMPORARY'
    SUSPENDED = 'SUSPENDED'
    CLOSED = 'CLOSED'
    INACTIVE_REASON = ((TEMPORARY, 'Temporary closed'), (SUSPENDED, 'Suspended'), (CLOSED, 'Closed'))

    OWNED = 'Owned'
    RENTAL = 'Rental'
    LOCATION = ((RENTAL, 'Rental'), (OWNED, 'Owned'))

    qr_code = models.IntegerField(max_length=20)
    business_name = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    barangay = models.CharField(max_length=100, blank=True, null=True)
    purok = models.CharField(max_length=100, blank=True, null=True)
    stall_no = models.CharField(max_length=20, blank=True, null=True)
    gps_all = models.DecimalField(max_digits=4, decimal_places=20, blank=True, null=True)
    gps_longitude = models.DecimalField(max_digits=4, decimal_places=20, blank=True, null=True)
    gps_lattitude = models.DecimalField(max_digits=4, decimal_places=20, blank=True, null=True)
    gps_altitude = models.DecimalField(max_digits=4, decimal_places=20, blank=True, null=True)
    gps_accuracy = models.DecimalField(max_digits=4, decimal_places=20, blank=True, null=True)
    owner_picture = models.ImageField()
    goods_services_picture = models.ImageField()
    business_permit_picture = models.ImageField()
    others1_picture = models.ImageField()
    others2_picture = models.ImageField()
    business_owner_name = models.CharField(max_length=255)
    business_owner_number = models.CharField(max_length=100, blank=True, null=True)
    business_representative = models.CharField(max_length=255, blank=True, null=True)
    owner_gender = models.CharField(max_length=10, blank=True, null=True)
    ownership_type = models.CharField(max_length=20,choices=OWNERSHIP, default=SINGLE, blank=True, null=True)
    is_business_permit = models.BooleanField(blank=True, null=True)
    business_permit_status = models.CharField(max_length=20, choices=NOTICE_STATUS, default=FIRST, blank=True, null=True)
    is_notice = models.BooleanField(blank=True, null=True)
    notice_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    notice_remarks = models.CharField(max_length=255, blank=True, null=True)
    business_status = models.CharField(max_length=100, choices=BUSINESS_STATUS, default=ACTIVE2, blank=True, null=True) 
    payment_type = models.CharField(max_length=50, choices=PAYMENT_MODE, default=ANNUAL, blank=True, null=True)
    inactive_remarks = models.CharField(max_length=255, blank=True, null=True)
    inactive_reason = models.CharField(max_length=50, choices=INACTIVE_REASON, default=TEMPORARY, blank=True, null=True)
    fsic = models.BooleanField(blank=True, null=True)
    fsic_number = models.CharField(max_length=100, blank=True, null=True)
    annual_payment_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    annual_paid_to = models.CharField(max_length=255, blank=True, null=True)
    annual_or_no = models.CharField(max_length=50, blank=True, null=True)
    annual_amount_paid = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    semi_annual_first_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    semi_annual_first_paid_to = models.CharField(max_length=255, blank=True, null=True)
    semi_annual_first_or_no = models.CharField(max_length=50, blank=True, null=True)
    semi_annual_first_amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    semi_annual_second_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    semi_annual_second_paid_to = models.CharField(max_length=255, blank=True, null=True)
    semi_annual_second_or_no = models.CharField(max_length=50, blank=True, null=True)
    semi_annual_second_amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    quarterly_first_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    quarterly_first_paid_to = models.CharField(max_length=255, blank=True, null=True)
    quarterly_first_or_no = models.CharField(max_length=50, blank=True, null=True)
    quarterly_first_amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    quarterly_second_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    quarterly_second_paid_to = models.CharField(max_length=255, blank=True, null=True)
    quarterly_second_or_no = models.CharField(max_length=50, blank=True, null=True)
    quarterly_second_amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    quarterly_third_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    quarterly_third_paid_to = models.CharField(max_length=255, blank=True, null=True)
    quarterly_third_or_no = models.CharField(max_length=50, blank=True, null=True)
    quarterly_third_amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    quarterly_fourth_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    quarterly_fourth_paid_to = models.CharField(max_length=255, blank=True, null=True)
    quarterly_fourth_or_no = models.CharField(max_length=50, blank=True, null=True)
    quarterly_fourth_amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    capitalization_amount = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    gross_sale_amount = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    total_employees = models.IntegerField(max_length=6, blank=True, null=True)
    total_male = models.IntegerField(max_length=6, blank=True, null=True)
    total_female = models.IntegerField(max_length=6, blank=True, null=True)
    location_status = models.CharField(max_length=20, choices=LOCATION, default=OWNED, blank=True, null=True)
    location_rental_amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    lessor_name = models.CharField(max_length=255, blank=True, null=True)

