# Generated by Django 4.2.4 on 2023-10-05 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone_num',
            new_name='phone',
        ),
    ]