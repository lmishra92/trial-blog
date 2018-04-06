# Generated by Django 2.0.3 on 2018-03-11 08:18

import datetime
from django.db import migrations, models
import django.db.models.manager
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 11, 8, 18, 5, 956663, tzinfo=utc)),
        ),
    ]
