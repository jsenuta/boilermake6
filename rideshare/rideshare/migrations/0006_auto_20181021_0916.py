# Generated by Django 2.0.6 on 2018-10-21 13:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0005_auto_20181021_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_ride',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
