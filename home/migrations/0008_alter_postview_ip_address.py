# Generated by Django 4.1.5 on 2023-01-14 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_postview_delete_postviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postview',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
    ]
