# Generated by Django 4.1.5 on 2023-01-13 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_userip'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserIp',
        ),
    ]
