# Generated by Django 2.1 on 2022-10-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]