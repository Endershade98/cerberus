# interfaces/api/energy/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from application.bootstrap import ApplicationFactory
from interfaces.api.energy.serializers import EnergyRecordSerializer


class EnergyRecordView(APIView):

    def post(self, request):
        serializer = EnergyRecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        use_case = ApplicationFactory.record_energy()

        record = use_case.execute(
            member_id=str(data["member_id"]),
            kwh=data["kwh"],
        )

        return Response(
            {
                "id": str(record.id),
                "member_id": str(record.member_id),
                "kwh": float(record.quantity.value)
                if hasattr(record.quantity, "value")
                else float(record.quantity),
            },
            status=status.HTTP_201_CREATED,
        )


class EnergyCalculateView(APIView):

    def get(self, request):
        use_case = ApplicationFactory.calculate_shared_energy()

        total = use_case.execute()

        # FIX: supporto robusto per Value Object
        if hasattr(total, "value"):
            total_value = float(total.value)
        elif hasattr(total, "amount"):
            total_value = float(total.amount)
        else:
            total_value = float(total)

        return Response(
            {"total_kwh": total_value},
            status=status.HTTP_200_OK,
        )