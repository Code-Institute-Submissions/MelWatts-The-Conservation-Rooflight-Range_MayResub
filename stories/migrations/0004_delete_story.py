# Generated by Django 3.2 on 2022-03-25 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_story'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Story',
        ),
    ]