# Generated by Django 3.2.12 on 2022-04-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_bookings_messenger_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='messenger_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='pickup_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
