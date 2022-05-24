# Generated by Django 4.0 on 2022-05-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_products_created_date'),
        ('orders', '0004_messengerorders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='products',
        ),
        migrations.AddField(
            model_name='orders',
            name='products',
            field=models.ManyToManyField(related_name='ordered_products', to='products.Products'),
        ),
    ]
