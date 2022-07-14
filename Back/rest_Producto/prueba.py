        promocion: Promocion = Promocion.objects.all()
        serializerPromocion = PromocionSerializer(promocion, many=True)
        finalList = []
        for promo in serializerPromocion.data:
            print(promo["idPromocion"])
            promocionProducto: PromocionProducto = PromocionProducto.objects.filter(
                idPromocion_id=promo["idPromocion"]
            )
            serializerPromocionProducto = PromocionProductoSerializer(
                promocionProducto, many=True
            )
            finalObject = {
                "idPromocion": promo["idPromocion"],
                "drescipcion": promo["descripcion"],
                "productos": serializerPromocionProducto.data,
            }
            finalList.append(finalObject)

        return Response(finalList, status=status.HTTP_200_OK)