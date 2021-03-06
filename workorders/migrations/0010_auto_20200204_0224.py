# Generated by Django 3.0.2 on 2020-02-04 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorders', '0009_auto_20200202_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorderpart',
            name='consumed_cost',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='workorderpart',
            name='processed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='wo_id',
            field=models.CharField(blank=True, editable=False, max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='workorderclock',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
