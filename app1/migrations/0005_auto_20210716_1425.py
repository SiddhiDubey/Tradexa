# Generated by Django 2.2.8 on 2021-07-16 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_post_mytimefield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='MyTimeField',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]