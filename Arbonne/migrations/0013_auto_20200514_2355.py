# Generated by Django 3.0.3 on 2020-05-14 22:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Arbonne', '0012_auto_20200514_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 22, 55, 26, 559367, tzinfo=utc)),
        ),
    ]