from rest_framework import serializers


from .models import FeeSchedule


class FeeScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeSchedule
        read_only_fields = ('created_by',)
        fields = ('id','annual_date', 'semi_annual_date1', 'semi_annual_date2',
                    'quarter_date1', 'quarter_date2', 'quarter_date3', 'quarter_date4')