# interfaces/api/energy/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from application.energy.record_energy import RecordEnergyUseCase
from application.energy.calculate_shared import CalculateSharedEnergyUseCase
from infrastructure.persistence.repositories.energy_repository import EnergyRepository

class RecordEnergyView(APIView):
    def post(self, request):
        member_id = request.data["member_id"]
        kwh = float(request.data["kwh"])
        use_case = RecordEnergyUseCase(EnergyRepository())
        record = use_case.execute(member_id, kwh)
        return Response({"member_id": record.member_id, "value_kwh": float(record.value_kwh)})

class CalculateSharedEnergyView(APIView):
    def get(self, request):
        use_case = CalculateSharedEnergyUseCase(EnergyRepository())
        total = use_case.execute()
        return Response({"total_kwh": float(total)})