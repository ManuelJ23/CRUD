# Generated by Django 5.0.6 on 2024-06-24 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_created',
            new_name='completed',
        ),
    ]
