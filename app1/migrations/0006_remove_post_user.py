# Generated by Django 2.2.8 on 2021-07-16 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20210716_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]