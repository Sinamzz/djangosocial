# Generated by Django 4.1.5 on 2023-01-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True),
        ),
    ]
