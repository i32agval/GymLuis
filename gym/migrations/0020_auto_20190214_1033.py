# Generated by Django 2.1.5 on 2019-02-14 10:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0019_auto_20190214_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 14, 10, 33, 2, 819550, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='weightdata',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 14, 10, 33, 2, 818588, tzinfo=utc)),
        ),
    ]
