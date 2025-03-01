from rest_framework import viewsets
from . import models, serializer
from rest_framework import exceptions


class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.InventorySerializer
    queryset = models.Inventory.objects.all().select_related('supplier')

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        if (len(self.request.query_params) > 1 or (len(self.request.query_params) == 1
                                                   and 'name' not in self.request.query_params)):
            raise exceptions.ValidationError(detail="Invalid query parameter used. Only 'name' is allowed.")
        if name:

            queryset = queryset.filter(name__iexact=name)
        return queryset
