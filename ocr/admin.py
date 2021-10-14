from django.contrib import admin
from .models import Image
from .models import ImageText

admin.site.register(Image)
admin.site.register(ImageText)
