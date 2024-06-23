from django.contrib import admin
from .models import *

admin.site.register(Titulo)
admin.site.register(Materia)


@admin.register(Profesor)
class profesor(admin.ModelAdmin):
    list_display = ('id', 'dni', 'nombre', 'apellido', 'tel', 'get_titulos')

    def get_titulos(self, obj):
        return ', '.join([titulo.nombre for titulo in obj.titulos.all()])

@admin.register(Tipo_de_Carrera)
class tipo_carrera(admin.ModelAdmin):
    list_display = ('tipo', 'duracion')

@admin.register(Carrera)
class carrera(admin.ModelAdmin):
    list_display = ('nombre', 'resolucion')
    
@admin.register(Alumno)
class alumno(admin.ModelAdmin):
    list_display = ('id', 'dni', 'nombre', 'apellido', 'tel', 'get_carreras')

    def get_carreras(self, obj):
        return ', '.join([Carrera.nombre for Carrera in obj.carreras.all()])
    
admin.site.site_header = 'IES'
admin.site.index_title = 'Panel de control'
admin.site.site_title = 'Administración del IES'