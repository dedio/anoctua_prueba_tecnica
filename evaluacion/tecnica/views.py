#~ Puntos 2 y 3
from rest_framework import viewsets 
from .serializers import CotizacionesSerializer, ComprasSerializer
from .models import CotizacionesModel, ComprasModel 

class PromediarPeriodoViewSet(viewsets.ModelViewSet): 
    serializer_class = CotizacionesSerializer 

    def get_queryset(self):
        fecha_inicio = self.request.query_params.get('fecha_inicio')
        fecha_fin = self.request.query_params.get('fecha_fin')

        queryset = CotizacionesModel.objects.filter(
            indice_tiempo=fecha_inicio, 
            indice_tiempo=fecha_fin
        ).aggregate(Avg('tipo_cambio_bna_vendedor'))['cambio__avg']

        return queryset

class ComprasViewSet(viewsets.ModelViewSet): 
	serializer_class = ComprasSerializer 

    def create(self, validated_data):
        fecha_de_compra = validated_data.get("fecha_de_compra", None)
        monto = validated_data.get("monto", None)
        validated.pop("fecha_de_compra")
        validated.pop("monto")

        cotizacion = CotizacionesModel.objects.filter(indice_tiempo=fecha_de_compra)
        
        if not cotizacion:
            cotizacion = CotizacionesModel.objects.filter(indice_tiempo<fecha_de_compra)

        return ComprasModel.objects.create(
            fecha_de_compra=fecha_de_compra, 
            monto=monto, 
            cotizacion=cotizacion
        )
