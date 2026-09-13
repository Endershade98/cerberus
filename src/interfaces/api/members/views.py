# interfaces/api/members/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from domain.membership.exceptions import MemberDomainError
from domain.membership.value_objects import MemberId

from src.application.members.register_member import RegisterMember
from src.application.members.validate_member import ValidateMember
from src.application.members.activate_member import ActivateMember

from src.interfaces.api.members.serializers import RegisterMemberSerializer
from src.interfaces.api.shared.uow_factory import build_uow


class MemberRegisterView(APIView):

    def post(self, request):

        serializer = RegisterMemberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        use_case = RegisterMember(uow=build_uow())

        member = use_case.execute(serializer.to_dto())

        return Response(
            {
                "id": str(member.id.value),
                "status": member.status.value,
            },
            status=status.HTTP_201_CREATED,
        )


class MemberValidateView(APIView):

    def post(self, request, member_id):

        use_case = ValidateMember(uow=build_uow())

        try:
            member = use_case.execute(MemberId(member_id))
        except MemberDomainError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"status": member.status.value},
            status=status.HTTP_200_OK,
        )

class MemberActivateView(APIView):

    def post(self, request, member_id):

        use_case = ActivateMember(uow=build_uow())

        try:
            member = use_case.execute(MemberId(member_id))
        except MemberDomainError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"status": member.status.value},
            status=status.HTTP_200_OK,
        )