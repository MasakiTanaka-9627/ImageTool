from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
from . import ocrtool


def index(request):
    text = ocrtool.function()
    images = Image.objects.all()
    context = {'images': images,
                'text':  text}

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
