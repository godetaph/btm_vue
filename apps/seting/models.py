from django.contrib.auth.models import User
from django.db import models

#fee_schedule
class FeeSchedule(models.Model):
        annual_date = models.DateField(auto_now=False, blank=True, null=True)
        semi_annual_date1 = models.DateField(auto_now=False, blank=True, null=True)
        semi_annual_date2 = models.DateField(auto_now=False, blank=True, null=True)
        quarter_date1 = models.DateField(auto_now=False, blank=True, null=True)
        quarter_date2 = models.DateField(auto_now=False, blank=True, null=True)
        quarter_date3 = models.DateField(auto_now=False, blank=True, null=True)
        quarter_date4 = models.DateField(auto_now=False, blank=True, null=True)
        created_by = models.ForeignKey(User, related_name="fee_schedule_users", on_delete=models.CASCADE)
        