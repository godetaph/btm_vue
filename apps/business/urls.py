from django.db.models import base
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BarangayViewSet, CategoryViewSet, BusinessViewSet

router = DefaultRouter()
router.register("businesses", BusinessViewSet, basename="businesses")
router.register("categories", CategoryViewSet, basename="categories")
router.register("barangays", BarangayViewSet, basename="barangays")

urlpatterns = [
    path('', include(router.urls)),
]