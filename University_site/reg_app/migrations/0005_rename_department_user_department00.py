# Generated by Django 4.1.7 on 2023-03-21 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0004_rename_department00_user_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='department',
            new_name='department00',
        ),
    ]