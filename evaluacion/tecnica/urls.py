#~ Puntos 2 y 3
from django.urls import path

from .views import PromediarPeriodoViewSet, ComprasViewSet

urlpatterns = [
    path("promediar_periodo/", PromediarPeriodoViewSet.as_view(), name="promediar_periodo"),
    path("add_compra/", ComprasViewSet.as_view(), name="add_compra"),
]
