# Generated by Django 3.0.4 on 2020-05-17 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CB_app', '0008_auto_20200517_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_bookmark',
            name='cb_bookmark_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cb_bookmark_ids', to='CB_app.Bookmark'),
        ),
    ]
