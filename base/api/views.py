from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UploadModel
from .forms import UploadForm
from .utils import extract_strip, get_colors
import cv2
import numpy as np
import json
from colorthief import ColorThief
import os

def home(request):
    if request.method == "POST":
        form = UploadForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            img_name=str(obj.image)
            x=cv2.imread(r"C:/Users/kamte/Urine-Test-App/base/public/static/{img_name}")
            print(x)
            return redirect('/',{"obj":obj,"x":x})
    else:
        form = UploadForm()
        img=UploadModel.objects.all()
    return render(request, "index.html", {"img":img,"form":form})

