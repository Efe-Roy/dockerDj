# Generated by Django 3.2.15 on 2023-05-04 14:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('filed', '0002_loggerall'),
    ]

    operations = [
        migrations.AddField(
            model_name='loggerall',
            name='createdAt',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
