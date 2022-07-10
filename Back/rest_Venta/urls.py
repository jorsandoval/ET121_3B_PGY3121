from django.urls import path
from rest_Venta import estadoVentaGetAll, estadoVentaByid, ventaGetAll, ventaByid, detalleVentaGetAll, detalleVentaByid

urlpatterns = [
    path('estadoVenta/', estadoVentaGetAll, name='estadoVentaGetAll'),
    path('estadoVenta/<idEstadoVenta>', estadoVentaByid, name='estadoVentaByid'),
    path('ventaGetAll/', ventaGetAll, name='ventaGetAll'),
    path('ventaGetAll/<idVenta>', ventaByid, name='ventaByid'),
    path('detalleVentaGetAll/', detalleVentaGetAll, name='detalleVentaGetAll'),
    path('detalleVentaByid/<idDetalleVenta>', detalleVentaByid, name='detalleVentaByid'),
]