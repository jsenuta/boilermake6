# Generated by Django 2.0 on 2018-10-21 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
