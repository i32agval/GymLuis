# Generated by Django 2.1.5 on 2019-02-14 09:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_auto_20190214_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 14, 9, 54, 32, 617073, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='weightdata',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 14, 9, 54, 32, 616103, tzinfo=utc)),
        ),
    ]
