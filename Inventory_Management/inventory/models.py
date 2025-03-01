from django.db import models
from django.utils import timezone


class Supplier(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    supplier = models.ForeignKey(Supplier, related_name="items", on_delete=models.CASCADE)
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
