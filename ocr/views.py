from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from PIL import Image as OCR_Image
import sys
import pyocr


def index(request):
    # text = ocrtool.function()
    tools = pyocr.get_available_tools()
    tool = tools[0]
    text = tool.image_to_string(
    OCR_Image.open('media/images/test.png'), lang='jpn')
    images = Image.objects.all()
    context = {'images': images, 'text': text}
    
    return render(request, 'index.html', context)


def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ocr:index')
    else:
        form = ImageForm()

    context = {'form': form}
    return render(request, 'upload.html', context)
