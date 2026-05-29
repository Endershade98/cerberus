# interfaces/api/energy/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from application.bootstrap import ApplicationFactory
from domain.energy.entities import EnergyRecord
from domain.energy.services import EnergyService


class EnergyRecordView(APIView):

    def post(self, request):
        data = request.data

        # VALIDATION SAFE (fix KeyError + ValueError)
        try:
            member_id = data.get("member_id")
            kwh = float(data.get("kwh"))
        except (TypeError, ValueError):
            return Response(
                {"error": "Invalid input"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if member_id is None:
            return Response(
                {"error": "member_id required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        use_case = ApplicationFactory.record_energy()

        record = use_case.execute(
            member_id=member_id,
            kwh=kwh,
        )

        return Response(
            {
                "id": str(record.id),
                "member_id": str(record.member_id),
                "value_kwh": float(record.value_kwh.amount)
                if hasattr(record.value_kwh, "amount")
                else float(record.value_kwh),
            },
            status=status.HTTP_201_CREATED,
        )


class EnergyCalculateView(APIView):

    def get(self, request):
        use_case = ApplicationFactory.calculate_shared_energy()

        total = use_case.execute()

        # FIX: EnergyQuantity -> float conversion
        if hasattr(total, "amount"):
            total_value = float(total.amount)
        else:
            total_value = float(total)

        return Response(
            {"total_kwh": total_value},
            status=status.HTTP_200_OK,
        )