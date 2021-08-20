from django.contrib.auth import models
from rest_framework import serializers

from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        read_only_fields = ['created_by', 'created_on',]
        fields = ['id','name', 'org_number', 'team_logo', 'team_address', 'zip_code',]

    