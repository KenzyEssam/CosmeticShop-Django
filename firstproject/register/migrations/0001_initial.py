# Generated by Django 4.2.4 on 2023-08-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
