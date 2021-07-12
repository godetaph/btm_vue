from django.db import models
from rest_framework import serializers
from rest_framework.relations import ManyRelatedField, StringRelatedField
from .models import Barangay, Business, BusinessCategory, BusinessPeriod, Category, Payment, Notification, Period



class BarangaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Barangay
        fields = ("id","barangay_name", "is_deleted")

class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        read_only_fields = ("created_by", "created_on")
        fields = ("id","payment_mode", "payment_date", "paid_to", "or_no", "amount_paid", "business")

class BusinessSerializer(serializers.ModelSerializer):
    barangay = BarangaySerializer(many=False)
    #category = CategorySerializer(many=True)
    class Meta:
        model = Business
        read_only_fields = ("created_by", "created_at", "modified_by", "modified_at", "team")
        fields = (
            "id","qr_code", "business_name", "municipality", "barangay", "purok", "stall_no", "gps_all", "gps_longitude", "gps_lattitude",
            "gps_altitude", "gps_accuracy", "owner_picture", "goods_services_picture", "business_permit_picture", 
            "others1_picture", "others2_picture", "business_owner_name", "business_owner_number", "business_representative",
            "owner_gender", "ownership_type", "is_business_permit", "business_permit_status", "is_notice",
            "notice_remarks", "business_status", "payment_type", "inactive_remarks", "inactive_reason", "fsic", "fsic_number",
            "capitalization_amount", "gross_sale_amount", "total_employees", "application_status",
            "total_male", "total_female", "location_status", "location_rental_amount", "lessor_name", "owner_signature",
            "collector_signature", "collector_designation", "picture1", "picture2", "picture3", "picture4", "picture5", "picture6",
        )

class BusinessCategorySerializer(serializers.ModelSerializer):
    category=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    #cat_name=serializers.StringRelatedField(source='category_business', read_only=True)
    cat_name=serializers.CharField(source='category.category_name', read_only=True)
    class Meta:
        model=BusinessCategory
        read_only_fields=("created_by", "created_on")
        fields=("id", "category", "business", "comment", "is_pushed", "cat_name")

class CategorySerializer(serializers.ModelSerializer):
    #bus_category=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #bus_cat= BusinessCategorySerializer(source='category_business', many=True)
    class Meta:
        model = Category
        fields = ("id","category_name", "is_deleted")

class NotificationSerializer(serializers.ModelSerializer):
    business_name=serializers.CharField(source='business.business_name', read_only=True)
    created=serializers.CharField(source='FORMAT')
    class Meta:
        model=Notification
        read_only_fields=("created_by",)
        fields=("id", "message", "is_read", "business", "append_type","created_on", "business_name", "created")

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Period
        read_only_fields=("created_by", "created_on",)
        fields=("id", "period_year", "note", "is_active")

class BusinessPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=BusinessPeriod
        read_only_fields=("created_by", "created_on", "collector")
        fields=("id", "period", "business", "comment")
