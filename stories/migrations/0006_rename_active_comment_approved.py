# Generated by Django 3.2 on 2022-03-29 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='active',
            new_name='approved',
        ),
    ]
