# Generated by Django 5.0.2 on 2024-04-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_rename_dob_student_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes/'),
        ),
    ]
