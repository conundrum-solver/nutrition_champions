# Generated by Django 5.0.2 on 2024-05-12 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_alter_student_student_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=9),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.CreateModel(
            name='ScanRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.student')),
            ],
        ),
    ]
