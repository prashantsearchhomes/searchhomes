# Generated by Django 3.1.6 on 2021-02-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shi_app', '0002_downloads_propertyimages_propsitedetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='region',
            field=models.CharField(default=' ', max_length=1100),
        ),
    ]
