# interfaces/api/energy/urls.py
from django.urls import path
from .views import RecordEnergyView, CalculateSharedEnergyView

urlpatterns = [
    path('record/', RecordEnergyView.as_view(), name='record-energy'),
    path('calculate/', CalculateSharedEnergyView.as_view(), name='calculate-shared-energy'),
]