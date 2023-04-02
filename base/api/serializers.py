from rest_framework import serializers
from .models import *

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadModel
        fields = ('id','title','caption','image')