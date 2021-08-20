from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeamSerializer
from .models import Team

class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset=Team.objects.all()

    def get_queryset(self):
        team = Team.objects.all()

        print(team)
        if not team:
            Team.objects.create(name='Organization name', org_number='00000', team_address='Address', zip_code='zip_code', created_by=self.request.user)
        
        return team
    
    def perform_created(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save()