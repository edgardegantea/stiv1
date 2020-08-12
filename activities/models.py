from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripción')
    active = models.BooleanField(default=False)

    def __str__(self):
        return "Activa: {0} - {1}".format(self.active, self.name)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


# Create your models here.
class Activity(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, verbose_name='Actividad')
    link = models.URLField()
    description = models.TextField()
    statusActivity = [('Iniciada', 'Iniciada'), ('En proceso', 'En proceso'), ('Finalizada', 'Finalizada')]
    status = models.CharField(max_length=50, choices=statusActivity)

    def __str__(self):
        return "Estado: {0} - {1}".format(self.status, self.name)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'