from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import FeeScheduleViewSet

router = DefaultRouter()
router.register("settings", FeeScheduleViewSet, basename="settings")

urlpatterns = [
    path('', include(router.urls))
]
