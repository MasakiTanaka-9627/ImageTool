# Generated by Django 3.2.8 on 2021-10-13 22:08

from django.db import migrations, models
import ocr.models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0002_imagetext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(upload_to=ocr.models._user_profile_avator_upload_to),
        ),
    ]
