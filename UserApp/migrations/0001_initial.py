# Generated by Django 4.0.4 on 2022-06-30 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personal_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=10)),
                ('Gender', models.CharField(max_length=6)),
                ('dob', models.DateField()),
                ('emailid', models.EmailField(max_length=50)),
                ('Address', models.TextField(max_length=225)),
                ('hobbies', models.CharField(max_length=100)),
                ('languages_known', models.CharField(max_length=50)),
                ('linkedin', models.CharField(max_length=200)),
                ('github', models.CharField(max_length=200)),
                ('objective', models.TextField(max_length=1000)),
            ],
            options={
                'db_table': 'personal_info',
            },
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'userInfo',
            },
        ),
        migrations.CreateModel(
            name='technical_skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=100)),
                ('perIn_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.personal_info')),
            ],
            options={
                'db_table': 'technical_skills',
            },
        ),
        migrations.CreateModel(
            name='my_resumes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.personal_info')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.user_info')),
            ],
            options={
                'db_table': 'my_resumes',
            },
        ),
        migrations.CreateModel(
            name='educational_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfExamination', models.CharField(max_length=50)),
                ('institute', models.CharField(max_length=500)),
                ('university', models.CharField(max_length=100)),
                ('percentage', models.CharField(max_length=10)),
                ('yearOfcompletion', models.CharField(max_length=10)),
                ('perIn_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.personal_info')),
            ],
            options={
                'db_table': 'educational_details',
            },
        ),
        migrations.CreateModel(
            name='certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification', models.CharField(max_length=100)),
                ('perIn_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.personal_info')),
            ],
            options={
                'db_table': 'certification',
            },
        ),
        migrations.CreateModel(
            name='academic_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('technologies_used', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('project_title', models.CharField(max_length=100)),
                ('perIn_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.personal_info')),
            ],
            options={
                'db_table': 'academic_project',
            },
        ),
    ]
