# Generated by Django 3.1.7 on 2021-03-19 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_comment_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
    ]