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
            path=str(obj.image)
            image = cv2.imread(f"C:/Users/kamte/OneDrive/Documents/Desktop/Urine Test App/base/public/static/{path}")
            strip = extract_strip(image)
            colors = get_colors(strip)
            color_labels = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']
            color_data = {color_labels[i]: colors[i] for i in range(len(colors))}
            result = json.dumps(color_data, indent=2)
            print(result)
            return render(request,'index.html',{"obj":obj,"result":result})
    else:
        form = UploadForm()
        img=UploadModel.objects.all()
    return render(request, "index.html", {"img":img,"form":form})

