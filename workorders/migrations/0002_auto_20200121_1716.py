# Generated by Django 3.0.2 on 2020-01-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workorders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='workorder',
            name='work_instructions',
            field=models.TextField(null=True),
        ),
    ]
