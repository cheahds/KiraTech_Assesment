from rest_framework import serializers
from . import models


class InventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)

    class Meta:
        model = models.Inventory
        fields = ['name', 'supplier_name', 'availability']
