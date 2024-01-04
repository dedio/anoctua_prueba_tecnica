#~ Puntos 2 y 3
from django.db import models 

class CotizacionesModel(models.Model): 
	indice_tiempo = models.DateField()
	tipo_cambio_bna_vendedor = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self): 
		return self.indice_tiempo

    class Meta:
        verbose_name = 'Cotizaciones'

class ComprasModel(models.Model):
	cotizacion = models.DecimalField(max_digits=10, decimal_places=2)
	monto = models.DecimalField(max_digits=10, decimal_places=2)
	fecha_de_compra = models.DateField()

	def __str__(self): 
		return self.fecha_de_compra

    class Meta:
        verbose_name = 'Compras'
