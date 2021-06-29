from rest_framework import serializers
from .models import Barangay, Business, Category, Payment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","category_name", "is_deleted")

class BarangaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Barangay
        fields = ("id","barangay_name", "is_deleted")

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        read_only_fields = ("created_by, created_on", "business")
        fields = ("id","payment_mode", "payment_date", "paid_to", "or_no", "amount_paid")

class BusinessSerializer(serializers.ModelSerializer):
    barangay = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    class Meta:
        model = Business
        read_only_fields = ("createed_by", "created_at", "modified_by", "modified_at", "team")
        fields = (
            "id","qr_code", "business_name", "municipality", "barangay", "purok", "stall_no", "gps_all", "gps_longitude", "gps_lattitude",
            "gps_altitude", "gps_accuracy", "owner_picture", "goods_services_picture", "business_permit_picture", 
            "others1_picture", "others2_picture", "business_owner_name", "business_owner_number", "business_representative",
            "owner_gender", "ownership_type", "is_business_permit", "business_permit_status", "is_notice",
            "notice_remarks", "business_status", "payment_type", "inactive_remarks", "inactive_reason", "fsic", "fsic_number",
            "capitalization_amount", "gross_sale_amount", "total_employees", "application_status",
            "total_male", "total_female", "location_status", "location_rental_amount", "lessor_name", "owner_signature",
            "collector_signature", "collector_designation", "picture1", "picture2", "picture3", "picture4", "picture5", "picture6", "category",
        )

