# Generated by Django 3.2.4 on 2021-09-23 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
