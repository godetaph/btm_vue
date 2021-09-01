from django.db.models import query
from django.db.models.aggregates import Sum
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, request

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response

from rest_framework import viewsets, filters
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework.fields import BuiltinSignatureError, MISSING_ERROR_MESSAGE
from rest_framework.serializers import Serializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import pagination
from .serializers import BusinessCategorySerializer, BusinessPeriodSerializer, CategorySerializer, BusinessSerializer, BarangaySerializer, PaymentSerializer, NotificationSerializer, PeriodSerializer, QrcodeSerializer
from .models import Barangay, BusinessPeriod, Category, Business, Payment, BusinessCategory, Notification, Period, Qrcode

# generic methods
def generate_qr_code():
    import random
    qr_code='%8x' % random.getrandbits(16*8)
    return qr_code

#method for auto-insert in the database
def create_notification(request, message, is_read, business, append_type):
    biz=get_object_or_404(Business, pk=business)
    notification=Notification.objects.create(message=message, is_read=is_read, business=biz, append_type=append_type)

def create_qrcode(qrcode):
    qrcode=Qrcode.objects.create(qrcode=qrcode)
    return qrcode
#paginations
class BusinessPagination(PageNumberPagination):
    page_size_query_param='size'

class NotificationPagination(PageNumberPagination):
    page_size=5

class BarangayPagination(PageNumberPagination):
    page_size_query_param='size'

class CategoryPagination(PageNumberPagination):
    page_size_query_param='size'


#viewsets
class QrcodeViewSet(viewsets.ModelViewSet):
    serializer_class=QrcodeSerializer
    queryset=Qrcode.objects.all()

    def get_queryset(self):
        qr_code=self.request.query_params.get('qr_code')
        print(qr_code)
        queryset = Qrcode.objects.all()
        if qr_code is not None:
            queryset = queryset.filter(qrcode=qr_code)
        else:
            qrcode=generate_qr_code()
            create_qrcode(qrcode)
            print(qrcode + ' saved.')
            queryset = Qrcode.objects.all()
            if qrcode is not None:
                queryset = queryset.filter(qrcode=qrcode)
                print(queryset.count)
        return queryset
            
    # def perform_create(self, serializer):
    #     qrcode=generate_qr_code()
    #     create_qrcode(qrcode)

#category_viewset
class CategoryViewSet(viewsets.ModelViewSet):
    pagination_class=CategoryPagination
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        # business=self.request.query_params.get('business')
        # queryset=
        return self.queryset.filter(is_deleted=False)

#barangay_viewset
class BarangayViewSet(viewsets.ModelViewSet):
    pagination_class=BarangayPagination
    serializer_class = BarangaySerializer
    queryset = Barangay.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_deleted=False)


# class CreateListMixin:
#     """Allows bulk creation of a resource."""
#     def get_serializer(self, *args, **kwargs):
#         if isinstance(kwargs.get('data', {}), list):
#             kwargs['many'] = True

#         return super().get_serializer(*args, **kwargs)

# class PaymentsViewSet(viewsets.ModelViewSet):
#     serializer_class = PaymentSerializer
#     queryset = Payment.objects.all()


#payment_viewset
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
        print("yo!")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        # serializer.save(created_by=self.request.user)

#business_viewset
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
class BusinessViewSet(viewsets.ModelViewSet):
    pagination_class=BusinessPagination
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()
    filter_backends=(filters.SearchFilter,)
    search_fields=('=qr_code','business_name', 'business_owner_name', 'business_representative', '^purok', '^lessor_name', '=is_business_permit',
                    '^barangay__barangay_name', '=ownership_type', '=business_permit_status', '=business_status', '=payment_type',
                    '=application_status', '=location_status', '^business_owner_number', 'capitalization_amount', 'gross_sale_amount')

    def get_queryset(self):
        bar=self.request.query_params.get('bar')
        permit=self.request.query_params.get('permit')
        qrcode=self.request.query_params.get('qrcode')
        scancode=self.request.query_params.get('scan')
        queryset=Business.objects.all()

        if qrcode is not None:
            qr_code=generate_qr_code()
            obj_qrcode=create_qrcode(qr_code)
            business_name_code=f"Business {obj_qrcode}"
            business=Business.objects.create(qr_code=qr_code, qrcode=obj_qrcode, business_name=business_name_code)
            queryset=Business.objects.filter(qrcode=obj_qrcode)

        if bar is not None:
            queryset=queryset.filter(barangay=bar)
        
        if permit is not None:
            queryset=queryset.filter(is_business_permit=permit)

        if scancode is not None:
            queryset=Business.objects.filter(qr_code=scancode)

        return queryset

    def perform_create(self, serializer):
        #team = self.request.user.teams.first()
        
        # barangay1 = self.request.POST.get('barangay')
        # barangay_id = Barangay.objects.get(id = barangay1)
        # if self.request.FILES:
        #     owner_picture = self.request.FILES.get('owner_picture')
        #     goods_picture = self.request.FILES.get('goods_picture')
        #     business_permit=self.request.FILES.get('business_permit')
        #     owner_signature=self.request.FILES.get('owner_signature')
        #     picture1=self.request.FILES.get('picture1')
        #     picture2=self.request.FILES.get('picture2')
        #     picture3=self.request.FILES.get('picture3')

        #     serializer.save(created_by=self.request.user,
        #                 owner_picture = owner_picture, goods_services_picture = goods_picture, 
        #                 business_permit_picture = business_permit,
        #                 owner_signature = owner_signature, picture1 = picture1, picture2=picture2, picture3=picture3)

        #serializer.save(created_by=self.request.user, barangay = barangay_id)
        serializer.save()

    def perform_update(self, serializer):
        #obj = self.get_object()

        # barangay1 = self.request.POST.get('barangay')
        # barangay_id = Barangay.objects.get(id= barangay1)
        # print("before")
        # print(serializer.validated_data['gps_latitude'])
        

        if self.request.FILES:
            print("inside")
            owner_picture = self.request.FILES.get('owner_picture')
            print(owner_picture, " owner")
            if owner_picture is not None:
                #with open(owner_picture.file.seek(0), "rb") as opened_pic:
                serializer.save(owner_picture = owner_picture)
            
            goods_picture = self.request.FILES.get('goods_picture')
            if goods_picture is not None:
                serializer.save(goods_services_picture = goods_picture)
            
            business_permit_picture=self.request.FILES.get('permit')
            if business_permit_picture is not None:
                serializer.save(business_permit_picture=business_permit_picture)

            owner_signature=self.request.FILES.get('owner_signature')
            if owner_picture is not None:
                serializer.save(owner_signature=owner_signature)
            
            picture1=self.request.FILES.get('picture1')
            if picture1 is not None:
                serializer.save(picture1=picture1)
            
            picture2=self.request.FILES.get('picture2')
            if picture2 is not None:
                serializer.save(picture2=picture2)
            
            picture3=self.request.FILES.get('picture3')
            if picture3 is not None:
                serializer.save(picture3=picture3)

        serializer.save()

#business_category_viewset
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
        serializer.save()
        if serializer.data['is_pushed']:
            create_notification(self.request, message=serializer.data['comment'], is_read=False, business=serializer.data['business'], append_type='Category')
        
        # qrcode=generate_qr_code()
        # create_qrcode(qrcode)
            
    
    def perform_update(self, serializer):
        serializer.save()
        if serializer.data['is_pushed']:
            create_notification(self.request, message=serializer.data['comment'], is_read=False, business=serializer.data['business'], append_type='Category')

#business_notifications
class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class=NotificationSerializer
    queryset=Notification.objects.all()
    pagination_class=NotificationPagination
    filter_backends=(filters.SearchFilter,)
    search_fields=["message", "^append_type", "^business__business_name"]

    def get_queryset(self):
        is_read=self.request.query_params.get('is_read')
        queryset=Notification.objects.all()

        if is_read is not None:
            queryset=queryset.filter(is_read=is_read)
        
        return queryset

#period_viewset
class PeriodViewSet(viewsets. ModelViewSet):
    serializer_class=PeriodSerializer
    queryset=Period.objects.all()

    def get_queryset(self):
        active = self.request.query_params.get('active')
        queryset = Period.objects.all()
        print(active)
        if active is not None:
            queryset = queryset.filter(is_active=True)
        
        return queryset

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

#business_period_viewset
class BusinessPeriodViewSet(viewsets.ModelViewSet):
    serializer_class=BusinessPeriodSerializer
    queryset=BusinessPeriod.objects.all()
    filter_backends = (DynamicSearchFilter,)
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields= ['period', 'business']

    def perform_create(self, serializer):
        serializer.save()
        create_notification(self.request, message=serializer.data['comment'], is_read=False, business=serializer.data['business'], append_type='Period')


