# Generated by Django 4.2.4 on 2023-08-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=250)),
                ('car_model', models.CharField(max_length=100)),
                ('production_year', models.CharField(max_length=10)),
                ('car_body', models.CharField(max_length=100)),
                ('engine_type', models.CharField(max_length=100)),
            ],
        ),
    ]
