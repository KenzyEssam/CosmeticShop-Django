# Generated by Django 4.2.4 on 2023-08-16 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otherpages', '0004_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('icon', models.CharField(max_length=200)),
            ],
        ),
    ]
