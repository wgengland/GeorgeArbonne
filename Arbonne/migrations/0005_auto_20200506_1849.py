# Generated by Django 3.0.3 on 2020-05-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arbonne', '0004_auto_20200505_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='testint',
        ),
        migrations.RemoveField(
            model_name='product',
            name='testint2',
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(default='null', editable=False, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.FloatField(default=100, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(editable=False, max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='Will be filled automatically', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_url',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published - most recent will appear first on your landing page!'),
        ),
    ]