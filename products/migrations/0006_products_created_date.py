# Generated by Django 4.0 on 2022-05-19 13:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
