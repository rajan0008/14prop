# Generated by Django 4.0.3 on 2024-04-20 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertiesServer14', '0003_remove_property_propertyrel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='properylistdetails',
            name='PropImage',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images'),
        ),
    ]