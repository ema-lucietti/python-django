from django.db import models

class Autor(models.Model):
    NACIONALIDADES = [
        ('ARG', 'Argentina'),
        ('BOL', 'Bolivia'),
        ('BRA', 'Brasil'),
        ('CHL', 'Chile'),
        ('COL', 'Colombia'),
        ('ECU', 'Ecuador'),
        ('ESP', 'España'),
        ('MEX', 'México'),
        ('PER', 'Perú'),
        ('USA', 'Estados Unidos'),
        ('OTR', 'Otra'),
    ]
    
    nombre = models.CharField(max_length=100, verbose_name="Nombre del autor")
    nacionalidad = models.CharField(max_length=3, choices=NACIONALIDADES, verbose_name="Nacionalidad")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    fecha_fallecimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de fallecimiento")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de última modificación")
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nombre']

class Frase(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='frases')
    texto = models.TextField(verbose_name="Texto de la frase")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.texto[:50]}..." if len(self.texto) > 50 else self.texto
    
    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = "Frases"