# Generated by Django 3.1.7 on 2021-03-19 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_delete_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_parent',
            field=models.BooleanField(default=False),
        ),
    ]