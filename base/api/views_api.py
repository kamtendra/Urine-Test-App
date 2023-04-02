from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status, viewsets
from .serializers import UploadSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import UploadModel
class UploadAPIView(viewsets.ModelViewSet):
    queryset = UploadModel.objects.all()
    serializer_class = UploadSerializer