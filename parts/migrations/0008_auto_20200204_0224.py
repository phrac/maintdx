# Generated by Django 3.0.2 on 2020-02-04 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0007_part_on_hand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partinventoryitem',
            name='current_on_hand',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='partinventoryitem',
            name='purchase_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
