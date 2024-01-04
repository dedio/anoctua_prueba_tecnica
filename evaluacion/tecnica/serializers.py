#~ Puntos 2 y 3
from rest_framework import serializers 
from .models import CotizacionesModel, ComprasModel

class CotizacionesSerializer(serializers.ModelSerializer): 

	class Meta: 
		model = CotizacionesModel 
		fields = ('indice_tiempo', 'tipo_cambio_bna_vendedor') 

class ComprasSerializer(serializers.ModelSerializer): 

    def create(self, validated_data):
        return ComprasModel.objects.create(**validated_data)

	class Meta: 
		model = ComprasModel 
		fields = ('cotizacion', 'monto', 'fecha_de_compra') 
