# Generated by Django 4.0 on 2023-05-27 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news1', '0009_news_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=20),
        ),
    ]
