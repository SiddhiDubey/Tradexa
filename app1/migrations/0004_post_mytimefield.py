# Generated by Django 2.2.8 on 2021-07-16 02:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20210716_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='MyTimeField',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
