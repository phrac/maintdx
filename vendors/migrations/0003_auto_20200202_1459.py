# Generated by Django 3.0.2 on 2020-02-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_auto_20200123_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendorcontact',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='vendorcontact',
            name='last_name',
            field=models.CharField(default='Unknow', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='vendorcontact',
            unique_together=set(),
        ),
    ]