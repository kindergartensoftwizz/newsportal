# Generated by Django 4.0 on 2023-04-28 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news1', '0004_alter_news_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='videonews',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news1.category'),
        ),
    ]
