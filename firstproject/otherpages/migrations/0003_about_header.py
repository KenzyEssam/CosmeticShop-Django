# Generated by Django 4.2.4 on 2023-08-16 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otherpages', '0002_team_alter_blog_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.TextField()),
                ('title2', models.TextField()),
                ('body', models.TextField()),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
