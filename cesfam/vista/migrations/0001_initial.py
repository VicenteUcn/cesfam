# Generated by Django 3.2.4 on 2021-07-06 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('rut_paciente', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Ingrese Rut Paciente ')),
                ('nombre', models.CharField(max_length=100, verbose_name='Ingrese Nombre Paciente ')),
                ('sexo_paciente', models.CharField(choices=[('1', 'Hombre'), ('2', 'Mujer')], max_length=50)),
                ('direccion', models.CharField(max_length=100, verbose_name='Ingrese dirección ')),
                ('fecha_de_nacimiento', models.DateField()),
                ('numero_telefono', models.CharField(max_length=100, verbose_name='Ingrese número de teléfono ')),
            ],
        ),
        migrations.CreateModel(
            name='Doctores',
            fields=[
                ('rut_doctor', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Ingrese Rut Doctor ')),
                ('nombre', models.CharField(max_length=50, verbose_name='Ingrese Nombre Doctor(a) ')),
                ('sexo_doctor', models.CharField(choices=[('1', 'Hombre'), ('2', 'Mujer')], max_length=50)),
                ('numero_tel', models.CharField(max_length=50, verbose_name='Ingrese número de doctor(a) ')),
                ('direcc', models.CharField(max_length=50, verbose_name='Ingrese dirección doctor(a) ')),
                ('especialidad', models.ManyToManyField(to='vista.Especialidades')),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_cita', models.TimeField()),
                ('fecha_cita', models.DateField()),
                ('rut_doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vista.doctores')),
                ('rut_paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vista.pacientes')),
            ],
        ),
    ]