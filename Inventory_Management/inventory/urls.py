from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_home, name='inventory-home'),
    path('<int:id>/', views.inventory_detail, name='inventory-detail')
]
