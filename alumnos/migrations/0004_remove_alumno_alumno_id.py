# Generated by Django 2.2.14 on 2020-12-02 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_alumno_alumno_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='alumno_id',
        ),
    ]
