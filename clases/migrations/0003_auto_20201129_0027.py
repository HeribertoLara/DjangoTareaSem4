# Generated by Django 2.2.14 on 2020-11-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0001_initial'),
        ('clases', '0002_auto_20201124_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clase',
            name='profesor',
        ),
        migrations.AddField(
            model_name='clase',
            name='profesor',
            field=models.ManyToManyField(related_name='profesor', to='profesores.Profesor'),
        ),
    ]
