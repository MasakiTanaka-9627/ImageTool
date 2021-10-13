# Generated by Django 3.2.8 on 2021-10-13 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('title', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ocr.image')),
            ],
        ),
    ]
