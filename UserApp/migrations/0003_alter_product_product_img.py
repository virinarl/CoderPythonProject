# Generated by Django 4.0.4 on 2022-08-04 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_product_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_Img',
            field=models.ImageField(null=True, upload_to='productsImg'),
        ),
    ]
