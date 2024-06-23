# Generated by Django 5.0 on 2024-06-23 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('resolucion', models.CharField(max_length=40, verbose_name='Resolución')),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
                'db_table': 'Carrera',
            },
        ),
        migrations.CreateModel(
            name='Tipo_de_Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=8, verbose_name='Tipo de carrera')),
                ('duracion', models.IntegerField(default=3, verbose_name='Duración')),
            ],
            options={
                'verbose_name': 'Tipo de Carrera',
                'verbose_name_plural': 'Tipos de Carreras',
                'db_table': 'Tipo_Carrera',
            },
        ),
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=8, verbose_name='Título')),
            ],
            options={
                'verbose_name': 'Título',
                'verbose_name_plural': 'Títulos',
                'db_table': 'Título',
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido')),
                ('tel', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('carrera', models.ManyToManyField(to='app1.carrera')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
                'db_table': 'Alumno',
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('año', models.IntegerField(verbose_name='Año')),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.carrera')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
                'db_table': 'Materia',
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido')),
                ('tel', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('titulos', models.ManyToManyField(to='app1.titulo')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
                'db_table': 'Profesor',
            },
        ),
    ]
