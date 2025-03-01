import requests

from django.shortcuts import render, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from . import models
from configs import CONFIGS


def inventory_home(Request: WSGIRequest):
    name_query = Request.GET.get('name', '')
    api_url = f'http://{CONFIGS.API_HOSTNAME}:{CONFIGS.API_PORT}/api/inventory/'
    query_path = {'name': name_query}

    response = requests.get(api_url, params=query_path)
    inventory_data = response.json()
    return render(Request, 'inventory/inventory-home.html', {'inventory_data': inventory_data})


def inventory_detail(Request: WSGIRequest, id: int):

    inventory_item = get_object_or_404(models.Inventory, id=id)
    return render(Request, 'inventory/inventory-detail.html', {'inventory_item': inventory_item})
