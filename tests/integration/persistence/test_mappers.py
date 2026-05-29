# tests/integration/persistence/test_mappers.py

from infrastructure.persistence.django.models.member import MemberModel
from infrastructure.persistence.django.mappers.mappers import to_domain


def test_member_mapper_to_domain(db):

    orm = MemberModel.objects.create(
        member_id="123e4567-e89b-12d3-a456-426614174000",
        name="Mario",
        email="mario@test.com",
        role="PRODUCER",
        status="ACTIVE",
    )

    domain = to_domain(orm)

    assert domain.name == "Mario"
    assert domain.email == "mario@test.com"