# Generated by Django 3.1.7 on 2021-03-18 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_comment_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
    ]