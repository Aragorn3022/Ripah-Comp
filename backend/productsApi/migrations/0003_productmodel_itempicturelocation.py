# Generated by Django 5.1.2 on 2024-10-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsApi', '0002_productmodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='itemPictureLocation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
