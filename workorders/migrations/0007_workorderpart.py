# Generated by Django 3.0.2 on 2020-01-24 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0005_auto_20200124_1939'),
        ('workorders', '0006_auto_20200123_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrderPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parts.Part')),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workorders.WorkOrder')),
            ],
        ),
    ]