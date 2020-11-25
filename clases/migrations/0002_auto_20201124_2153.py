# Generated by Django 2.2.14 on 2020-11-25 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_auto_20201121_2325'),
        ('clases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='alumno',
            field=models.ManyToManyField(related_name='alumnos', to='alumnos.Alumno'),
        ),
        migrations.AddField(
            model_name='clase',
            name='horario',
            field=models.DateTimeField(null=True),
        ),
    ]