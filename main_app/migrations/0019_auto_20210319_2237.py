# Generated by Django 3.1.7 on 2021-03-19 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_profile_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo_url',
            field=models.CharField(default='https://s3-us-west-1.amazonaws.com/wayfarer-pp/d80df8.png', max_length=200),
        ),
    ]
