# Generated by Django 5.0.7 on 2024-07-11 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_user_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ConfigChoice',
        ),
    ]
