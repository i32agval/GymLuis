# Generated by Django 2.1.5 on 2019-02-14 10:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0014_auto_20190214_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2019, 2, 14, 10, 2, 18, 685656, tzinfo=utc)),
        ),
    ]
