from django.db import models

from django.db import models

class Horario(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    dias = models.CharField(max_length=100)
    horarios = models.TextField(help_text=" Ej: 07:00, 08:00, cada 15 minutos....")
    tarifa_adulto = models.IntegerField(blank=True, null=True, verbose_name="Tarifa Adulto")
    tarifa_mayor = models.IntegerField(blank=True, null=True, verbose_name="Tarifa Adulto Mayor")
    tarifa_escolar = models.IntegerField(blank=True, null=True, verbose_name="Tarifa Escolar")

    def __str__(self):
        return f"{self.origen} - {self.destino} ({self.dias})"