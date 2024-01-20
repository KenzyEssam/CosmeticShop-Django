# Generated by Django 4.2.4 on 2023-08-16 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otherpages', '0003_about_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='static/img/')),
            ],
        ),
    ]
