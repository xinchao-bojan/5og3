# Generated by Django 3.2 on 2021-04-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_student_studentm'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentm',
            name='ed_competence',
            field=models.ManyToManyField(to='main_app.EdCompetence'),
        ),
        migrations.AddField(
            model_name='studentm',
            name='emp_competence',
            field=models.ManyToManyField(to='main_app.EmpCompetence'),
        ),
    ]