from django.db import models

class Contact(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True)
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.correo}"

CONTENT_CHOICES = [
    ('series', 'Serie'),
]

class Series(models.Model):
    title = models.CharField('Título', max_length=200)
    summary = models.CharField('Resumen corto', max_length=300, blank=True)
    description = models.TextField('Descripción', blank=True)
    keywords = models.CharField('Palabras clave', max_length=300, blank=True)
    image = models.ImageField(upload_to='series_images/', blank=True, null=True)
    content_type = models.CharField(max_length=10, choices=CONTENT_CHOICES, default='series')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.content_type})"

class FAQ(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pregunta frecuente"
        verbose_name_plural = "Preguntas frecuentes"
        ordering = ['-creado']

    def __str__(self):
        return self.pregunta
