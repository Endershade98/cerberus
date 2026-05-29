# interfaces/api/energy/urls.py

from django.urls import path
from .views import RecordEnergyView, CalculateSharedEnergyView

urlpatterns = [
    path("record/", RecordEnergyView.as_view()),
    path("calculate/", CalculateSharedEnergyView.as_view()),
]