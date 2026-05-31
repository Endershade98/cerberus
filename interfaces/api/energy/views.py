# interfaces/api/energy/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from application.energy.record_energy import RecordEnergyUseCase
from application.energy.calculate_shared import CalculateSharedEnergyUseCase

from interfaces.api.energy.serializers import EnergyRecordSerializer
from interfaces.api.shared.uow_factory import build_uow


class EnergyRecordView(APIView):

    def post(self, request):

        serializer = EnergyRecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = RecordEnergyUseCase(uow=build_uow())

        record = use_case.execute(
            member_id=str(serializer.validated_data["member_id"]),
            kwh=serializer.validated_data["kwh"],
        )

        return Response(
            {
                "id": str(record.id),
                "member_id": str(record.member_id),
                "kwh": record.quantity.value,
            },
            status=status.HTTP_201_CREATED,
        )


class EnergyCalculateView(APIView):

    def get(self, request):

        use_case = CalculateSharedEnergyUseCase(uow=build_uow())

        total = use_case.execute()

        return Response(
            {"total_kwh": total.value},
            status=status.HTTP_200_OK,
        )