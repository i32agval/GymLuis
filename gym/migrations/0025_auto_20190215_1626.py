# Generated by Django 2.1.5 on 2019-02-15 16:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0024_auto_20190214_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 15, 16, 26, 38, 16189, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='weightdata',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 15, 16, 26, 38, 15212, tzinfo=utc)),
        ),
    ]
