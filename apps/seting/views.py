from django.shortcuts import render
from rest_framework import viewsets
import datetime

from .models import FeeSchedule
from .serializers import FeeScheduleSerializer

class FeeScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = FeeScheduleSerializer
    queryset = FeeSchedule.objects.all()

    def get_queryset(self):
        fee_schedule = FeeSchedule.objects.all()

        if not fee_schedule:
            date = datetime.date.today()
            FeeSchedule.objects.create(annual_date=date, semi_annual_date1=date,
                                        semi_annual_date2=date, quarter_date1=date,
                                        quarter_date2=date,quarter_date3=date,
                                        quarter_date4=date, created_by=self.request.user)
            
            
        return fee_schedule
        
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save()
