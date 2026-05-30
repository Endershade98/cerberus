# interfaces/api/members/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from application.bootstrap import ApplicationFactory

from domain.member.exceptions import MemberDomainError
from domain.member.value_objects import MemberId, TaxInformation, Address


class MemberRegisterView(APIView):

    def post(self, request):
        data = request.data

        required_fields = [
            "name", "email", "fiscal_code",
            "street", "city", "postal_code", "country"
        ]

        missing = [f for f in required_fields if f not in data]

        if missing:
            return Response(
                {"error": "missing fields", "fields": missing},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            use_case = ApplicationFactory.register_member()

            command = {
                "name": data["name"],
                "email": data["email"],
                "tax_info": TaxInformation(
                    fiscal_code=data["fiscal_code"]
                ),
                "address": Address(
                    street=data["street"],
                    city=data["city"],
                    postal_code=data["postal_code"],
                    country=data["country"],
                ),
            }

            member = use_case.execute(command)

        except (ValueError, MemberDomainError) as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "id": str(member.id.value),
                "status": member.status.value,
            },
            status=status.HTTP_201_CREATED,
        )


class MemberValidateView(APIView):

    def post(self, request, member_id):

        use_case = ApplicationFactory.validate_member()

        try:
            member = use_case.execute(MemberId(member_id))

        except MemberDomainError:
            return Response(
                {"error": "Member not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {"status": member.status.value},
            status=status.HTTP_200_OK,
        )


class MemberActivateView(APIView):

    def post(self, request, member_id):

        use_case = ApplicationFactory.activate_member()

        try:
            member = use_case.execute(MemberId(member_id))

        except MemberDomainError:
            return Response(
                {"error": "Member not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {"status": member.status.value},
            status=status.HTTP_200_OK,
        )