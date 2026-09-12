# domain/member/exceptions.py

class MemberDomainError(Exception):
    pass


class InvalidMemberStateError(MemberDomainError):
    pass


class MemberAlreadyActiveError(MemberDomainError):
    pass


class MemberAlreadySuspendedError(MemberDomainError):
    pass


class InvalidMemberRoleChange(MemberDomainError):
    pass