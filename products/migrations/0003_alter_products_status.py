# Generated by Django 4.0 on 2022-04-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]