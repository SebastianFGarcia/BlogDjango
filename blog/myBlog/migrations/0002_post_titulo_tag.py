# Generated by Django 3.1 on 2020-08-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titulo_tag',
            field=models.CharField(default='Blog', max_length=255),
        ),
    ]