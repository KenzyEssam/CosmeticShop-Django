# Generated by Django 4.2.4 on 2023-08-16 18:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='image',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
