# Generated by Django 2.1.5 on 2019-02-10 10:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gym', '0002_auto_20190208_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('created_date', models.DateField(default=datetime.date(2019, 2, 10))),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gym.UserProfile')),
            ],
        ),
    ]
