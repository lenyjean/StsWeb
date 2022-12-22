# Generated by Django 4.1.2 on 2022-12-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordResetRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=1000)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_expired', models.BooleanField(default=False)),
            ],
        ),
    ]
