from .models import Image
from django.shortcuts import render


def index(request):
    images = Image.objects.all()
    context = {'images': images}

    return render(request, 'index.html', context)
