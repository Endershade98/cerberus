# tests/unit/test_register_member.py

from application.members.register_member import RegisterMember
from application.members.dtos import RegisterMemberUseCaseInput
from tests.support.fake_uow import FakeUnitOfWork

from domain.member.value_objects import MemberRole, TaxInformation, Address


def test_register_member_usecase():

    uow = FakeUnitOfWork()

    # FIX: intercettiamo eventi raccolti dal UoW
    collected_events = []

    def collect(events):
        collected_events.extend(events)

    uow.collect = collect

    uc = RegisterMember(uow)

    dto = RegisterMemberUseCaseInput(
        name="Mario",
        email="mario@test.com",
        role=MemberRole.CONSUMER,
        tax_info=TaxInformation("RSSMRA80A01H501U"),
        address=Address("Via Roma", "Napoli", "80100", "IT"),
    )

    member = uc.execute(dto)

    assert member.email == "mario@test.com"
    assert len(collected_events) == 1