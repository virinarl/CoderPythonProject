# Generated by Django 4.0.4 on 2022-08-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='Texto default', max_length=6000),
            preserve_default=False,
        ),
    ]
