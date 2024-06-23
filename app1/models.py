from django.db import models

class Titulo(models.Model):
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
    titulos = models.ManyToManyField(Titulo, blank=False)
    def __str__(self):
        return '%s %s'%(self.apellido, self.nombre)  
    class Meta:
        db_table = 'Profesor'
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

class Tipo_de_Carrera(models.Model):
    tipo = models.CharField(max_length=8, null=False, verbose_name='Tipo de carrera')
    duracion = models.IntegerField(null=False, default=3, verbose_name='Duración')
    def __str__(self):
        return '%s %s'%(self.tipo, self.duracion)  
    class Meta:
        db_table = 'Tipo_Carrera'
        verbose_name = 'Tipo de Carrera'
        verbose_name_plural = 'Tipos de Carreras' 
      
class Carrera(models.Model):
    nombre = models.CharField(max_length=50, null=False, verbose_name='Nombre')
    resolucion = models.CharField(max_length=40, null=False, verbose_name='Resolución')
    def __str__(self):
        return '%s '%(self.nombre)  
    class Meta:
        db_table = 'Carrera'
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'   

class Materia(models.Model):
    nombre = models.CharField(max_length=50, null=False, verbose_name='Nombre')
    año = models.IntegerField(null=False, verbose_name='Año')
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, blank=False)
    def __str__(self):
        return '%s '%(self.nombre)  
    class Meta:
        db_table = 'Materia'
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'      
        
class Alumno(models.Model):
    dni = models.CharField(max_length=8, null=False, verbose_name='DNI')
    nombre = models.CharField(max_length=20, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, null=False, verbose_name='Apellido')
    tel = models.CharField(max_length=10, null=False, verbose_name='Teléfono')
    carrera = models.ManyToManyField(Carrera, blank=False)
    def __str__(self):
        return '%s %s'%(self.apellido, self.nombre)  
    class Meta:
        db_table = 'Alumno'
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'