# interfaces/api/members/serializers.py

from rest_framework import serializers

from application.members.dtos import RegisterMemberUseCaseInput
from domain.member.value_objects import MemberRole, TaxInformation, Address


class RegisterMemberSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=[r.value for r in MemberRole])

    fiscal_code = serializers.CharField()
    street = serializers.CharField()
    city = serializers.CharField()
    postal_code = serializers.CharField()
    country = serializers.CharField()

    def to_dto(self) -> RegisterMemberUseCaseInput:
        return RegisterMemberUseCaseInput(
            name=self.validated_data["name"],
            email=self.validated_data["email"],
            role=MemberRole(self.validated_data["role"]),
            tax_info=TaxInformation(self.validated_data["fiscal_code"]),
            address=Address(
                street=self.validated_data["street"],
                city=self.validated_data["city"],
                postal_code=self.validated_data["postal_code"],
                country=self.validated_data["country"],
            ),
        )