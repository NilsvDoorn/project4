# Generated by Django 2.2.1 on 2019-05-24 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190524_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.AddField(
            model_name='products',
            name='price_large',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='price_small',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='extra_kaas',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
