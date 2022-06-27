# Generated by Django 4.0.4 on 2022-06-25 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0005_certification'),
    ]

    operations = [
        migrations.CreateModel(
            name='academic_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('technologies_used', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterModelTable(
            name='certification',
            table='certification',
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
    ]
