# Generated by Django 3.2 on 2021-05-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='can_backorder',
            field=models.BooleanField(default=False),
        ),
    ]
