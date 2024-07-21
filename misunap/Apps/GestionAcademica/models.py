from django.db import models

# Create your models here.

class Alumno(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    DNI = models.CharField(max_length=8)
    FechaNacimiento = models.DateField()
    SEXOS = (('F','Femenino'),('M','Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXOS,
default='M')

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno,
self.ApellidoMaterno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

class Curso(models.Model):
    Nombre = models.CharField(max_length=50)
    Creditos = models.PositiveSmallIntegerField()
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.Creditos)

class Matriculas(models.Model):
    Alumno = models.ForeignKey(Alumno, null=False,
blank=False, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, null=False, blank=False,
on_delete=models.CASCADE)
    FechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Alumno, self.Curso.Nombre)