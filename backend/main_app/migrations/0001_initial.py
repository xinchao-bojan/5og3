# Generated by Django 3.2 on 2021-04-17 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EdCompetence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название компетенции')),
            ],
        ),
        migrations.CreateModel(
            name='EdOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название образовательной организации')),
                ('competence', models.ManyToManyField(to='main_app.EdCompetence')),
            ],
        ),
        migrations.CreateModel(
            name='EmpCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название организации-работодателя')),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Оценка')),
            ],
        ),
        migrations.CreateModel(
            name='EmpCompetence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название компетенции')),
                ('ed_competence', models.ManyToManyField(blank=True, to='main_app.EdCompetence')),
            ],
        ),
        migrations.CreateModel(
            name='EmployerM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.empcompany')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='custom_user.employermore')),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование стажировки')),
                ('description', models.TextField(verbose_name='Описание стажировки')),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Оценка')),
                ('emp_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.empcompany', verbose_name='Работодатель')),
                ('input_emp_competence', models.ManyToManyField(related_name='input_emp_competence', to='main_app.EmpCompetence')),
                ('output_emp_competence', models.ManyToManyField(related_name='output_emp_competence', to='main_app.EmpCompetence')),
            ],
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование стажировки')),
                ('description', models.TextField(verbose_name='Описание практики')),
                ('ed_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.edorganization', verbose_name='Образовательная организация')),
                ('input_ed_competence', models.ManyToManyField(related_name='input_ed_competence', to='main_app.EdCompetence')),
                ('output_ed_competence', models.ManyToManyField(related_name='output_ed_competence', to='main_app.EdCompetence')),
            ],
        ),
        migrations.CreateModel(
            name='StudentM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Оценка')),
                ('ed_competence', models.ManyToManyField(to='main_app.EdCompetence')),
                ('ed_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.edorganization')),
                ('emp_competence', models.ManyToManyField(to='main_app.EmpCompetence')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='custom_user.studentmore')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Название навыка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.studentm')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewOnStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название отзыва')),
                ('review_text', models.TextField(verbose_name='Отзыв')),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Оценка')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.employerm', verbose_name='Работодатель')),
                ('student_for_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.studentm', verbose_name='Отзыв на студента')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewOnEmployer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Заголовок отзыва')),
                ('review_text', models.TextField(verbose_name='Отзыв')),
                ('rate', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Оценка')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.internship', verbose_name='Отзыв о стажировке')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.studentm', verbose_name='Студент')),
            ],
        ),
        migrations.CreateModel(
            name='PracticeApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.practice')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.studentm')),
            ],
        ),
        migrations.CreateModel(
            name='InternshipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('ed_organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.edorganization')),
                ('internship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.internship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.studentm')),
            ],
        ),
        migrations.CreateModel(
            name='EdWorkerM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ed_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.edorganization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='custom_user.edworkermore')),
            ],
        ),
        migrations.AddField(
            model_name='edcompetence',
            name='emp_competence',
            field=models.ManyToManyField(blank=True, to='main_app.EmpCompetence'),
        ),
    ]
