from django.shortcuts import render, redirect
from .models import Image, ImageText
from .forms import ImageForm
from PIL import Image as OCR_Image
import sys
import pyocr


def index(request):
    images = Image.objects.all()
    texts = ImageText.objects.all()
    context = {'images': images, 'texts': texts}
    
    return render(request, 'index.html', context)


def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        form.save()
        images = Image.objects.all()
        entries = Image.objects.all().order_by("-id")[0]
        print(entries.picture)
        tools = pyocr.get_available_tools()
        tool = tools[0]
        txt = tool.image_to_string(
        OCR_Image.open(entries.picture),
        lang='jpn',
        )
        ImageText.objects.create(title=entries, text=txt)
        return redirect('ocr:index')
    else:
        form = ImageForm()

    context = {'form': form}
    return render(request, 'upload.html', context)
