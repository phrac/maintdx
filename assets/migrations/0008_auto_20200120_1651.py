# Generated by Django 3.0.2 on 2020-01-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0003_partvendor_vendor'),
        ('assets', '0007_auto_20200120_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='parts',
            field=models.ManyToManyField(blank=True, to='parts.Part'),
        ),
    ]
