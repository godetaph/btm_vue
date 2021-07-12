from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, request

from rest_framework import viewsets, filters
from rest_framework import serializers
from rest_framework.fields import BuiltinSignatureError, MISSING_ERROR_MESSAGE
from rest_framework.serializers import Serializer
from rest_framework.pagination import PageNumberPagination
from .serializers import BusinessCategorySerializer, BusinessPeriodSerializer, CategorySerializer, BusinessSerializer, BarangaySerializer, PaymentSerializer, NotificationSerializer, PeriodSerializer
from .models import Barangay, BusinessPeriod, Category, Business, Payment, BusinessCategory, Notification, Period

class BusinessPagination(PageNumberPagination):
    page_size=5

class NotificationPagination(PageNumberPagination):
    page_size=5

class BarangayPagination(PageNumberPagination):
    page_size=10

class CategoryPagination(PageNumberPagination):
    page_size=10

class CategoryViewSet(viewsets.ModelViewSet):
    pagination_class=CategoryPagination
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        # business=self.request.query_params.get('business')
        # queryset=
        return self.queryset.filter(is_deleted=False)

class BarangayViewSet(viewsets.ModelViewSet):
    pagination_class=BarangayPagination
    serializer_class = BarangaySerializer
    queryset = Barangay.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_deleted=False)

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def get_queryset(self):
        business=self.request.query_params.get('business')
        queryset=Payment.objects.all()
        if business is not None:
            queryset = queryset.filter(business=business)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class BusinessViewSet(viewsets.ModelViewSet):
    pagination_class=BusinessPagination
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()
    filter_backends=(filters.SearchFilter,)
    search_fields=('business_name', 'business_owner_name')

    # def get_queryset(self):
    #     return self.queryset.filter(created_by = self.request.user)

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

class BusinessCategoryViewSet(viewsets.ModelViewSet):
    serializer_class=BusinessCategorySerializer
    queryset=BusinessCategory.objects.all()

    def get_queryset(self):
        business=self.request.query_params.get('business')
        queryset=BusinessCategory.objects.all()
        if business is not None:
            queryset=queryset.filter(business=business)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        if serializer.data['is_pushed']:
            create_notification(self.request, message=serializer.data['comment'], is_read=False, business=serializer.data['business'], append_type='Added')
            
    
    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)
        if serializer.data['is_pushed']:
            create_notification(self.request, message=serializer.data['comment'], is_read=False, business=serializer.data['business'], append_type='Changed')

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class=NotificationSerializer
    queryset=Notification.objects.all()
    pagination_class=NotificationPagination

    def get_queryset(self):
        is_read=self.request.query_params.get('is_read')
        print(is_read)
        queryset=Notification.objects.all()
        if is_read is not None:
            print(is_read)
            queryset=queryset.filter(is_read=is_read)
            print(queryset.count)
        
        return queryset

class PeriodViewSet(viewsets. ModelViewSet):
    serializer_class=PeriodSerializer
    queryset=Period.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class BusinessPeriodViewSet(viewsets.ModelViewSet):
    serializer_class=BusinessPeriodSerializer
    queryset=BusinessPeriod.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, collector=self.request.user)

#method for auto-insert in the database

def create_notification(request, message, is_read, business, append_type):
    biz=get_object_or_404(Business, pk=business)
    notification=Notification.objects.create(message=message, is_read=is_read, business=biz, created_by=request.user, append_type=append_type)
