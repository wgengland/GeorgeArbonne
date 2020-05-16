# Generated by Django 3.0.3 on 2020-05-14 23:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Arbonne', '0014_auto_20200515_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='analytics',
            name='last_hit',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 23, 16, 8, 348873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 14, 23, 16, 8, 348354, tzinfo=utc)),
        ),
    ]
