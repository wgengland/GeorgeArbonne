# Generated by Django 3.0.3 on 2020-05-05 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arbonne', '0003_auto_20200505_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='hello', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='testint',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='testint2',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
