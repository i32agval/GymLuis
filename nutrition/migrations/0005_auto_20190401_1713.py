# Generated by Django 2.1.7 on 2019-04-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0004_auto_20190216_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
