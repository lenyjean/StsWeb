# Generated by Django 4.0 on 2022-04-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
