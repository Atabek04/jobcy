# Generated by Django 4.1.2 on 2022-11-27 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_experience_alter_job_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='experience',
        ),
    ]
