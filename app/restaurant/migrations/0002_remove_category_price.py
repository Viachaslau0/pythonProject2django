# Generated by Django 5.0 on 2023-12-16 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='price',
        ),
    ]
