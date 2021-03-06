# Generated by Django 3.0.3 on 2020-05-15 16:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Arbonne', '0015_auto_20200515_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analytics',
            name='last_hit',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 16, 49, 6, 593431, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 16, 49, 6, 593431, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfHit', models.DateTimeField(default=datetime.datetime(2020, 5, 15, 16, 49, 6, 594426, tzinfo=utc))),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
