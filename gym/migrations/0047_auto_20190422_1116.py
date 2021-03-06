# Generated by Django 2.2 on 2019-04-22 11:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0046_auto_20190411_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 22, 11, 16, 42, 247769, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='weight',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='biceps',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='chest',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 22, 11, 16, 42, 246636, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='gastrocnemius',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='muscle_fat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='muscle_mass',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='quadricep',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='waist',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='weight',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='weightdata',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 22, 11, 16, 42, 246193, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='weightdata',
            name='weight',
            field=models.IntegerField(max_length=10),
        ),
    ]
