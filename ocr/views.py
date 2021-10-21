from django.shortcuts import render, redirect
from .models import Image, ImageText
from .forms import ImageForm
from PIL import Image as OCR_Image
import pyocr

def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        form.save()
        entries = Image.objects.all().order_by("-id")[0]
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

    images = Image.objects.all().order_by("-id")[0]

    try:
        texts = ImageText.objects.all().order_by("-id")[0]
    except:
        texts = "エラー"

    context = {'images': images, 'texts': texts, 'form': form}
    return render(request, 'index.html', context)
