# Generated by Django 4.1.2 on 2022-11-23 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='code',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
