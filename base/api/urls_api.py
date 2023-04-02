from django.urls import path, include
from .views_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'uploads', UploadAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
