from django.db import models

class Título(models.Model):
    nombre = models.CharField(max_length=8, null=False, verbose_name='Título')
    def __str__(self):
        return '%s'%(self.nombre)  
    class Meta:
        db_table = 'Título'
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos'

class Profesor(models.Model):
    dni = models.CharField(max_length=8, null=False, verbose_name='DNI')
    nombre = models.CharField(max_length=20, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, null=False, verbose_name='Apellido')
    tel = models.CharField(max_length=10, null=False, verbose_name='Teléfono')
    cargo = models.ForeignKey(Título, on_delete=models.CASCADE, blank=True, null=False)
    def __str__(self):
        return '%s %s'%(self.apellido, self.nombre)  
    class Meta:
        db_table = 'Profesor'
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'