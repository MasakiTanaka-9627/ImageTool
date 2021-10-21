from datetime import datetime
import hashlib
import os
from django.db import models

def _user_profile_avator_upload_to(instance, filename):
    current_time = datetime.now()
    pre_hash_name = '%s%s' % (filename, current_time)
    extension = str(filename).split('.')[-1]
    hs_filename = '%s.%s' % (hashlib.md5(
        pre_hash_name.encode()).hexdigest(), extension)
    saved_path = 'images/'
    return '%s%s' % (saved_path, hs_filename)

class Image(models.Model):
    picture = models.ImageField(
        upload_to=_user_profile_avator_upload_to
        )
    def __str__(self):
        return self.title

class ImageText(models.Model):
    text = models.TextField()
    title = models.OneToOneField(Image, models.CASCADE)
    def __str__(self):
        return self.text
