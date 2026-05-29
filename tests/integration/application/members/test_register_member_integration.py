# tests/integration/application/members/test_register_member_integration.py

from application.members.register_member import RegisterMember
from application.members.dtos import RegisterMemberUseCaseInput

from domain.member.repository import MemberRepository
from domain.member.value_objects import MemberRole, TaxInformation, Address
from infrastructure.persistence.django.unit_of_work import DjangoUnitOfWork


def test_register_member_integration(db):

    repo = MemberRepository()
    uow = DjangoUnitOfWork()

    use_case = RegisterMember(repo, uow)

    dto = RegisterMemberUseCaseInput(
        name="Mario",
        email="mario@test.com",
        role=MemberRole.CONSUMER,
        tax_info=TaxInformation("RSSMRA80A01H501U"),
        address=Address("Via Roma", "Napoli", "80100", "IT")
    )

    member = use_case.execute(dto)

    assert member.id is not None