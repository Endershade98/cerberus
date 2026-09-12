# interfaces/api/energy/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from src.application.energy.calculate_shared import CalculateSharedEnergyUseCase

from src.interfaces.api.shared.uow_factory import build_uow


from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from decimal import Decimal


from src.application.energy.dtos import RecordEnergyRequest
from src.application.energy.record_energy import RecordEnergy



class EnergyRecordView(APIView):


    def post(self, request):

        command = RecordEnergyRequest(
            asset_id=request.data["asset_id"],
            timestamp=datetime.fromisoformat(
                request.data["timestamp"]
            ),
            production_kwh=Decimal(
                request.data["production"]
            ),
            consumption_kwh=Decimal(
                request.data["consumption"]
            )
        )


        use_case = RecordEnergy(
            repository=self.repository,
            uow=self.uow,
            publisher=self.publisher
        )


        result = use_case.execute(command)


        return Response(
            {
                "id": str(result.id)
            }
        )

class EnergyCalculateView(APIView):

    def get(self, request):

        use_case = CalculateSharedEnergyUseCase(uow=build_uow())

        total = use_case.execute()

        return Response(
            {"total_kwh": total.value},
            status=status.HTTP_200_OK,
        )