# Generated by Django 4.0 on 2023-04-29 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news1', '0005_videonews_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videonews',
            old_name='category',
            new_name='categoryid',
        ),
    ]