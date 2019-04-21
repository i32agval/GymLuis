# Generated by Django 2.1.7 on 2019-03-28 11:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0037_auto_20190327_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='gym.jpg', null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 28, 11, 58, 17, 721814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userimages',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 28, 11, 58, 17, 720658, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='weightdata',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 3, 28, 11, 58, 17, 720198, tzinfo=utc)),
        ),
    ]
