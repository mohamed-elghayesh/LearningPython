# Generated by Django 3.0.2 on 2020-01-24 22:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0003_news_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 24, 22, 57, 2, 669081, tzinfo=utc)),
        ),
    ]