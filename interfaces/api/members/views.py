# interfaces/api/members/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterMemberSerializer, ActivateMemberSerializer

class RegisterMemberUseCaseView(APIView):
    serializer_class = RegisterMemberSerializer  # <- aggiungi questa riga

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # qui chiami il tuo use case
        return Response({"message": "Member registered"}, status=status.HTTP_201_CREATED)

class ActivateMemberUseCaseView(APIView):
    serializer_class = ActivateMemberSerializer  # <- aggiungi questa riga

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # qui chiami il tuo use case
        return Response({"message": "Member activated"}, status=status.HTTP_200_OK)