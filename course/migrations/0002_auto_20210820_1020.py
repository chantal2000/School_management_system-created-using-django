# Generated by Django 3.2.4 on 2021-08-20 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Course_code',
            new_name='course_code',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='Course_duration',
            new_name='course_duration',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='Course_schedule',
            new_name='course_schedule',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='Syllabus',
            new_name='syllabus',
        ),
    ]
