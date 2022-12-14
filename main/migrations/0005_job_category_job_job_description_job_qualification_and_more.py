# Generated by Django 4.1.2 on 2022-11-23 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_job_logo_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.jobcategory'),
        ),
        migrations.AddField(
            model_name='job',
            name='job_description',
            field=models.TextField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='qualification',
            field=models.TextField(max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.company'),
        ),
        migrations.AlterField(
            model_name='job',
            name='date_posted',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='employment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.employment'),
        ),
    ]
