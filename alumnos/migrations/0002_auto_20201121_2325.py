# Generated by Django 2.2.14 on 2020-11-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='clase',
        ),
        migrations.AddField(
            model_name='alumno',
            name='edad',
            field=models.IntegerField(null=True),
        ),
    ]
