import pytest

from django.urls import reverse
from django.test import Client
from rest_framework.test import APIClient
from inventory.models import Inventory, Supplier


def test_inventory_home_status():
    client = Client()
    url = reverse('inventory-home')
    response = client.get(url)

    assert response.status_code == 200


def test_api_inventory_home_status():
    api_client = APIClient()
    url = reverse('inventory-home')
    response = api_client.get(url)

    assert response.status_code == 200

@pytest.mark.django_db
@pytest.mark.parametrize("test_input, test_output",
                         [(1, 200),
                          (999, 404)
                          ])
def test_api_inventory_detail_status(test_input, test_output):
    supplier = Supplier.objects.create(name="Supplier A")
    if test_input == 1:
        _ = Inventory.objects.create(
            name="Item 1",
            description="Description for Item 1",
            note="Note for Item 1",
            stock=50,
            availability=True,
            supplier=supplier
        )

    client = Client()
    url = reverse('inventory-detail', kwargs={'id': test_input})
    response = client.get(url)
    assert response.status_code == test_output
