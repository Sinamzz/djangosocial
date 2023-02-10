# Generated by Django 4.1.5 on 2023-01-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_ip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ip',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='ip',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
