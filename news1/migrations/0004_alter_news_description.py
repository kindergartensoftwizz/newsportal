# Generated by Django 4.0 on 2023-04-27 03:28

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('news1', '0003_videonews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]