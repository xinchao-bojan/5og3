# Generated by Django 3.2 on 2021-04-17 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210417_2129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='name',
            new_name='text',
        ),
    ]