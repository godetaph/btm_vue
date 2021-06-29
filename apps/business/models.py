from apps.team.models import Team
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
        category_name = models.CharField(max_length=255)
        is_deleted = models.BooleanField(default=False)

        class Meta:
                ordering = ("category_name",)

        def __str__(self):
                return self.category_name
        
class Barangay(models.Model):
        barangay_name = models.CharField(max_length=150, unique=True)
        is_deleted = models.BooleanField(default=False)

        class Meta: 
                ordering = ("barangay_name",)

        def __str__(self):
                return self.barangay_name

class Business(models.Model):
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

        MALE = 'Male'
        FEMALE = 'Female'
        GENDER = ((MALE, 'Male'), (FEMALE, 'Female'))

        qr_code = models.IntegerField(blank=True, null=True)
        business_name = models.CharField(max_length=255, blank=True, null=True)
        municipality = models.CharField(max_length=255, blank=True, null=True)
        barangay = models.ForeignKey(Barangay, related_name="business_barangay", on_delete=models.CASCADE, blank=True, null=True)
        purok = models.CharField(max_length=100, blank=True, null=True)
        stall_no = models.CharField(max_length=20, blank=True, null=True)
        gps_all = models.DecimalField(max_digits=20, decimal_places=20, blank=True, null=True)
        gps_longitude = models.DecimalField(max_digits=20, decimal_places=20, blank=True, null=True)
        gps_lattitude = models.DecimalField(max_digits=20, decimal_places=20, blank=True, null=True)
        gps_altitude = models.DecimalField(max_digits=20, decimal_places=20, blank=True, null=True)
        gps_accuracy = models.DecimalField(max_digits=20, decimal_places=20, blank=True, null=True)
        owner_picture = models.ImageField(upload_to='media/owner_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True) 
        goods_services_picture = models.ImageField(upload_to='media/goods_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
        business_permit_picture = models.ImageField(upload_to='media/permit_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
        others1_picture = models.ImageField(upload_to='media/others_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
        others2_picture = models.ImageField(upload_to='media/others_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
        business_owner_name = models.CharField(max_length=255, blank=True, null=True)
        business_owner_number = models.CharField(max_length=100, blank=True, null=True)
        business_representative = models.CharField(max_length=255, blank=True, null=True)
        owner_gender = models.CharField(max_length=10, blank=True, null=True)
        ownership_type = models.CharField(max_length=20, blank=True, null=True)
        is_business_permit = models.CharField(max_length=10, blank=True, null=True)
        business_permit_status = models.CharField(max_length=20, blank=True, null=True)
        is_notice = models.CharField(max_length=50, blank=True, null=True)
        notice_remarks = models.CharField(max_length=255, blank=True, null=True)
        business_status = models.CharField(max_length=100, blank=True, null=True) 
        payment_type = models.CharField(max_length=50, blank=True, null=True)
        inactive_remarks = models.CharField(max_length=255, blank=True, null=True)
        inactive_reason = models.CharField(max_length=50, blank=True, null=True)
        fsic = models.CharField(max_length=10, blank=True, null=True)
        fsic_number = models.CharField(max_length=100, blank=True, null=True)
        application_status = models.CharField(max_length=50, blank=True, null=True)
        capitalization_amount = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
        gross_sale_amount = models.DecimalField(max_digits=11, decimal_places=2, default=0.0, blank=True, null=True)
        total_employees = models.IntegerField(blank=True, null=True)
        total_male = models.IntegerField(blank=True, null=True)
        total_female = models.IntegerField(blank=True, null=True)
        location_status = models.CharField(max_length=20, blank=True, null=True)
        location_rental_amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
        lessor_name = models.CharField(max_length=255, blank=True, null=True)
        owner_signature = models.ImageField(upload_to='media/owner_sig_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
        collector_signature = models.ImageField(upload_to='media/collector_sig_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
        collector_designation = models.CharField(max_length=50, blank=True, null=True)
        picture1 = models.ImageField(upload_to='media/add_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
        picture2 = models.ImageField(upload_to='media/add_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
        picture3 = models.ImageField(upload_to='media/add_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
        picture4 = models.ImageField(upload_to='media/add_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
        picture5 = models.ImageField(upload_to='media/add_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
        picture6 = models.ImageField(upload_to='media/add_pic/', height_field=None, width_field=None, max_length=None, blank=True, null=True)
        team = models.ForeignKey(Team, related_name='team_business', on_delete=models.CASCADE, blank=True, null=True)
        category = models.ForeignKey(Category, related_name='business_categories', on_delete=models.CASCADE, blank=True, null=True)
        created_by = models.ForeignKey(User, related_name='created_business', on_delete=models.CASCADE)
        modified_by = models.ForeignKey(User, related_name='modified_business', on_delete=models.CASCADE, blank=True, null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        modified_at = models.DateTimeField(auto_now_add=True)
        is_deleted = models.BooleanField(default=False)

        class Meta:
                ordering = ("business_name",)

        def __str__(self):
                return self.business_name


class Payment(models.Model):
        payment_mode = models.CharField(max_length=50)
        payment_date = models.DateTimeField(auto_now=False)
        paid_to = models.CharField(max_length=255, blank=True, null=True)
        or_no = models.CharField(max_length=50)
        amount_paid = models.DecimalField(max_digits=7, decimal_places=2)
        business = models.ForeignKey(Business, related_name="business_payments", on_delete=models.CASCADE)
        created_by = models.ForeignKey(User, related_name="user_payments", on_delete=models.CASCADE)
        created_on = models.DateTimeField(auto_now_add=True)

        class Meta:
                ordering = ["-payment_date",]

        def __str__(self):
                return self.payment_mode