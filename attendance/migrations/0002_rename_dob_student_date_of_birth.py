# Generated by Django 5.0.2 on 2024-04-30 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='dob',
            new_name='date_of_birth',
        ),
    ]
