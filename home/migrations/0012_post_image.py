# Generated by Django 4.1.5 on 2023-01-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d/'),
        ),
    ]
