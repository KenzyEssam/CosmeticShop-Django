# Generated by Django 4.2.4 on 2023-08-19 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otherpages', '0007_alter_blog_slider_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messagee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
