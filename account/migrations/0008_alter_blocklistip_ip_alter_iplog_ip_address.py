# Generated by Django 4.1.5 on 2023-01-08 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_blocklistip_ip_alter_iplog_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blocklistip',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='iplog',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
    ]