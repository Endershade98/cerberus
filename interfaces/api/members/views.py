# interfaces/api/members/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from application.members.register_member import RegisterMember
from application.members.validate_member import ValidateMember
from application.members.activate_member import ActivateMember

from infrastructure.persistence.repositories.member_repository import (
    DjangoMemberRepository,
)

from infrastructure.persistence.unit_of_work import (
    DjangoUnitOfWork,
)

from domain.member.value_objects import (
    TaxInformation,
    Address,
    MemberId,
)


class MemberRegisterView(APIView):

    def post(self, request):

        use_case = RegisterMember(
            repository=DjangoMemberRepository(),
            uow=DjangoUnitOfWork(),
        )

        member = use_case.execute(
            name=request.data["name"],
            email=request.data["email"],
            tax_info=TaxInformation(
                fiscal_code=request.data["fiscal_code"]
            ),
            address=Address(
                street=request.data["street"],
                city=request.data["city"],
                postal_code=request.data["postal_code"],
                country=request.data["country"],
            ),
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

        use_case = ValidateMember(
            repository=DjangoMemberRepository(),
            uow=DjangoUnitOfWork(),
        )

        member = use_case.execute(
            MemberId(member_id)
        )

        return Response(
            {
                "status": member.status.value
            }
        )


class MemberActivateView(APIView):

    def post(self, request, member_id):

        use_case = ActivateMember(
            repository=DjangoMemberRepository(),
            uow=DjangoUnitOfWork(),
        )

        member = use_case.execute(
            MemberId(member_id)
        )

        return Response(
            {
                "status": member.status.value
            }
        )