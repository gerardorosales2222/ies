from django.db import models
      
class Carrera(models.Model):
    nombre = models.CharField(max_length=50, null=False, verbose_name='Nombre')
    resolucion = models.CharField(max_length=40, null=False, verbose_name='Resolución')
    duracion = models.IntegerField(null=False, default=4, verbose_name='Duración')
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

class Profesor(models.Model):
    dni = models.CharField(max_length=8, null=False, verbose_name='DNI')
    nombre = models.CharField(max_length=20, null=False, verbose_name='Nombre')
    apellido = models.CharField(max_length=20, null=False, verbose_name='Apellido')
    tel = models.CharField(max_length=10, null=False, verbose_name='Teléfono')
    titulos = models.ManyToManyField(Materia, blank=False)
    def __str__(self):
        return '%s %s'%(self.apellido, self.nombre)  
    class Meta:
        db_table = 'Profesor'
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'    
        
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