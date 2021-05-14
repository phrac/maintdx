# Generated by Django 3.2.2 on 2021-05-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0016_auto_20210513_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetgroup',
            name='parts',
        ),
        migrations.AddField(
            model_name='assetattachment',
            name='asset_groups',
            field=models.ManyToManyField(blank=True, to='assets.AssetGroup'),
        ),
    ]
