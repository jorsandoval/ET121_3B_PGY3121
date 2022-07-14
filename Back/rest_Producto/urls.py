from django.urls import path
from .views import (
    productById,
    productGetAll,
    categoriaGetAll,
    categoriaById,
    promocionGetAll,
    promocionById,
    productByIdCategoria,
)

urlpatterns = [
    path("productos/", productGetAll, name="productGetAll"),
    path("productos/byId/<id>", productById, name="productById"),
    path("productos/byCategoria/<id>", productByIdCategoria, name="productByIdCategoria"),
    path("categoria/", categoriaGetAll, name="categoriaGetAll"),
    path("categoria/<id>", categoriaById, name="categoriaById"),
    path("promociones/", promocionGetAll, name="promocionesGetAll"),
    path("promociones/<id>", promocionById, name="promocionesGetById"),
]
