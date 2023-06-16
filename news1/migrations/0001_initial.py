# Generated by Django 3.0.3 on 2020-04-10 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='image/')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=200)),
                ('suggestion', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='image/')),
                ('postby', models.CharField(max_length=200)),
                ('poston', models.CharField(max_length=200)),
                ('tag', models.CharField(choices=[('new', 'NEW'), ('Breaking', 'BREAKING'), ('recent', 'RECENT'), ('latest', 'LATEST')], default='new', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news1.category')),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]