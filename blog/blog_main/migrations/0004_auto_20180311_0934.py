# Generated by Django 2.0.3 on 2018-03-11 09:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_main', '0003_auto_20180311_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 11, 9, 34, 9, 542129, tzinfo=utc)),
        ),
    ]
