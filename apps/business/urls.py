from apps.business.models import BusinessPeriod
from apps.business.serializers import NotificationSerializer
from django.db.models import base
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BarangayViewSet, BusinessCategoryViewSet, BusinessPeriodViewSet, CategoryViewSet, BusinessViewSet, NotificationViewSet, PaymentViewSet, PeriodViewSet, QrcodeViewSet

router = DefaultRouter()
router.register("businesses", BusinessViewSet, basename="businesses")
router.register("categories", CategoryViewSet, basename="categories")
router.register("barangays", BarangayViewSet, basename="barangays")
router.register("payments", PaymentViewSet, basename="payments")
router.register("business-categories", BusinessCategoryViewSet, basename="business-categories")
router.register("notifications", NotificationViewSet, basename="notifications")
router.register("periods", PeriodViewSet, basename="periods")
router.register("qrcodes", QrcodeViewSet, basename="qrcodes")
router.register("business-periods", BusinessPeriodViewSet, basename="business-periods")


urlpatterns = [
    path('', include(router.urls)),
]