# Generated by Django 3.2 on 2021-04-17 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_auto_20210417_0319'),
        ('main_app', '0003_auto_20210417_1032'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='StudentM',
        ),
    ]
