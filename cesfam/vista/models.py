from django.db import models


# Create your models here.
class Pacientes(models.Model):
    rut_paciente = models.CharField(max_length=50, null=False, blank=False, primary_key=True, verbose_name='Ingrese Rut Paciente ')
    nombre = models.CharField(max_length=100, null=False, blank=False, verbose_name='Ingrese Nombre Paciente ')
    sexos = [("1", "Hombre"), ("2", "Mujer")]
    sexo_paciente = models.CharField(max_length=50, null=False, blank=False, choices=sexos)
    direccion = models.CharField(max_length=100, null=False, blank=False, verbose_name='Ingrese dirección ')
    fecha_de_nacimiento = models.DateField()
    numero_telefono = models.CharField(max_length=100, null=False, blank=False,
                                       verbose_name='Ingrese número de teléfono ')

    def __str__(self):
        return self.nombre


class Especialidades(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=50, null=False, blank=False)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.nombre


class Doctores(models.Model):
    rut_doctor = models.CharField(max_length=50, null=False, blank=False, primary_key=True,
                                  verbose_name='Ingrese Rut Doctor ')
    nombre = models.CharField(max_length=50, null=False, blank=False, verbose_name='Ingrese Nombre Doctor(a) ')
    sexos = [("1", "Hombre"), ("2", "Mujer")]
    sexo_doctor = models.CharField(max_length=50, null=False, blank=False, choices=sexos)
    numero_tel = models.CharField(max_length=50, null=False, blank=False, verbose_name='Ingrese número de doctor(a) ')
    direcc = models.CharField(max_length=50, null=False, blank=False, verbose_name='Ingrese dirección doctor(a) ')
    especialidad=models.ManyToManyField(Especialidades)
    def __str__(self):
        return "{0}".format(self.nombre)


class Cita(models.Model):
    rut_doctor=models.ForeignKey(Doctores, on_delete=models.PROTECT)
    rut_paciente=models.ForeignKey(Pacientes, on_delete=models.PROTECT)
    hora_cita = models.TimeField()
    fecha_cita = models.DateField()

    def __str__(self):
        return self.str(id)



