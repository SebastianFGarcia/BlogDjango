# Generated by Django 3.1 on 2020-08-25 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0003_auto_20200820_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
