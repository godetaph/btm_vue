from django.shortcuts import render
from django.http import HttpResponse, request

from rest_framework import viewsets
from rest_framework.fields import BuiltinSignatureError
from rest_framework.serializers import Serializer
from .serializers import CategorySerializer, BusinessSerializer, BarangaySerializer, PaymentSerializer
from .models import Barangay, Category, Business, Payment

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_deleted=False)

class BarangayViewSet(viewsets.ModelViewSet):
    serializer_class = BarangaySerializer
    queryset = Barangay.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_deleted=False)

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def get_queryset(self):
        business = self.request.user.business_payments.first()
        return self.request.filter(business=business)

class BusinessViewSet(viewsets.ModelViewSet):
    
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by = self.request.user)

    def perform_create(self, serializer):
        team = self.request.user.teams.first()
        
        business_name = self.request.POST.get('business_name')
        business_owner_name = self.request.POST.get('business_owner_name')
        barangay1 = self.request.POST.get('barangay')
        category1 = self.request.POST.get('category')
        barangay_id = Barangay.objects.get(id = barangay1)
        category_id = Category.objects.get(id = category1)
        if self.request.FILES:
            owner_picture = self.request.FILES.get('owner_picture')
            goods_picture = self.request.FILES.get('goods_picture')

        serializer.save(created_by=self.request.user, 
                        owner_picture = owner_picture, business_name = business_name, 
                        business_owner_name = business_owner_name, barangay = barangay_id, category = category_id,
                        goods_services_picture = goods_picture,
                        team = team)

    def perform_update(self, serializer):
        obj = self.get_object()

        barangay1 = self.request.POST.get('barangay')
        category1 = self.request.POST.get('category')
        barangay_id = Barangay.objects.get(barangay_name = barangay1)
        category_id = Category.objects.get(category_name = category1)
        
        if self.request.FILES:
            owner_picture = self.request.FILES.get('owner_picture')
            goods_picture = self.request.FILES.get('goods_picture')
            serializer.save(owner_picture = owner_picture, goods_services_picture = goods_picture)

        serializer.save(created_by=self.request.user, 
                         barangay = barangay_id, category = category_id)
