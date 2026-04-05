# application/members/activate_member.py
from domain.member.entities import Member, RegisterMemberUseCaseInput
from domain.member.value_objects import MemberRole

class ActivateMemberUseCase:
    """
    Use case for activating a member.
    This use case checks if the member is in a pending state and, if so, activates the member and updates their role based on the input data. 
    It ensures that only members with a pending status can be activated.
    """
    def __init__(self, member: Member):
        self.member = member

    def execute(self, input_data: RegisterMemberUseCaseInput):
        """
        Activate the member if they are in a pending state and update their role.
        Args:            
            input_data (RegisterMemberUseCaseInput): The input data containing the new role for the member.
        Returns:
            None
        Raises:
            ValueError: If the member is not in a pending state.
        """
        if self.member.status != "MEM-PENDING":
            raise ValueError("Only pending members can be activated.")
        
        self.member.activate()
        self.member.change_role(MemberRole(input_data.role))