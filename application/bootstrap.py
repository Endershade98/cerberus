# application/bootstrap.py

from infrastructure.persistence.django.unit_of_work import DjangoUnitOfWork
from infrastructure.events.outbox.repository import OutboxRepository

from application.members.register_member import RegisterMember
from application.members.activate_member import ActivateMember
from application.members.exit_member import ExitMember
from application.members.suspend_member import SuspendMember
from application.members.reject_member import RejectMember

from application.energy.record_energy import RecordEnergy
from application.energy.calculate_shared import CalculateSharedEnergy


class ApplicationFactory:

    # ---------------- MEMBERS ----------------

    @staticmethod
    def register_member():
        return RegisterMember(
            uow=DjangoUnitOfWork(
                outbox_repo=OutboxRepository()
            )
        )

    @staticmethod
    def activate_member():
        return ActivateMember(
            uow=DjangoUnitOfWork(
                outbox_repo=OutboxRepository()
            )
        )

    @staticmethod
    def exit_member():
        return ExitMember(
            uow=DjangoUnitOfWork(
                outbox_repo=OutboxRepository()
            )
        )

    @staticmethod
    def suspend_member():
        return SuspendMember(
            uow=DjangoUnitOfWork(
                outbox_repo=OutboxRepository()
            )
        )

    @staticmethod
    def reject_member():
        return RejectMember(
            uow=DjangoUnitOfWork(
                outbox_repo=OutboxRepository()
            )
        )

    # ---------------- ENERGY ----------------

    @staticmethod
    def record_energy():
        return RecordEnergy(
            uow=DjangoUnitOfWork(
                outbox_repo=OutboxRepository()
            )
        )

    @staticmethod
    def calculate_shared_energy():
        return CalculateSharedEnergy(
            uow=DjangoUnitOfWork(
                outbox_repo=OutboxRepository()
            )
        )