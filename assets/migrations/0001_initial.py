# Generated by Django 3.0.2 on 2020-01-16 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('serial_number', models.CharField(max_length=64, null=True)),
                ('make', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('install_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Category')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Department')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Location')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='CategoryProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_name', models.CharField(max_length=16)),
                ('required', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Category')),
            ],
            options={
                'verbose_name_plural': 'Category Properties',
                'unique_together': {('category', 'key_name')},
            },
        ),
    ]