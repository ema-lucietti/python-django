from django.contrib import admin
from .models import Autor, Frase

class FraseInline(admin.TabularInline):
    model = Frase
    extra = 1

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'fecha_nacimiento', 'fecha_fallecimiento', 'activo')
    list_filter = ('activo', 'nacionalidad')
    search_fields = ('nombre',)
    inlines = [FraseInline]
    actions = ['activar_autores', 'desactivar_autores']
    
    def activar_autores(self, request, queryset):
        queryset.update(activo=True)
    activar_autores.short_description = "Marcar como activos"
    
    def desactivar_autores(self, request, queryset):
        queryset.update(activo=False)
    desactivar_autores.short_description = "Marcar como inactivos"

@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    list_display = ('texto', 'autor', 'fecha_creacion')
    list_filter = ('autor',)
    search_fields = ('texto', 'autor__nombre')