# Generated by Django 5.0.2 on 2024-05-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_student_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='FEMALE', max_length=9),
        ),
        migrations.AddField(
            model_name='student',
            name='student_class',
            field=models.CharField(default=1, max_length=20, unique=True),
        ),
    ]
