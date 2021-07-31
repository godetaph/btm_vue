from django.contrib.auth.models import User
from django.db import models

#team model
class Team(models.Model):
    name = models.CharField(max_length=255)
    org_number = models.CharField(max_length=255, blank=True, null=True)
    team_logo = models.ImageField(upload_to="media/team_logo/", blank=True, null=True)
    team_address = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='teams', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
