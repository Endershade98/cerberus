# application/members/dtos.py

from dataclasses import dataclass
from src.domain.member.value_objects import MemberRole, TaxInformation, Address


@dataclass(frozen=True)
class RegisterMemberUseCaseInput:
    name: str
    email: str
    role: MemberRole
    tax_info: TaxInformation
    address: Address