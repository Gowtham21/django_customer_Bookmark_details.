# Generated by Django 3.0.4 on 2020-05-16 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CB_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='bookmarks',
        ),
    ]
