# interfaces/api/energy/urls.py

from django.urls import path
from interfaces.api.energy.views import EnergyCalculateView, EnergyRecordView


urlpatterns = [
    path("record/", EnergyRecordView.as_view()),
    path("calculate/", EnergyCalculateView.as_view()),
]