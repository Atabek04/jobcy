# Generated by Django 4.1.2 on 2022-11-27 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_job_experience'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.RemoveField(
            model_name='job',
            name='experience',
        ),
    ]
