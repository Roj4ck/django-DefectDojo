# Generated by Django 2.2.1 on 2019-09-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0018_sonarqube_api_integration'),
    ]

    operations = [
        migrations.AddField(
            model_name='system_settings',
            name='credentials',
            field=models.CharField(max_length=3000, blank=True),
        ),
        migrations.AddField(
            model_name='system_settings',
            name='column_widths',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='system_settings',
            name='drive_folder_ID',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='system_settings',
            name='enable_google_sheets',
            field=models.BooleanField(null=True, blank=True, default=False),
        ),
    ]
