# interfaces/api/members/urls.py

from django.urls import path

from src.interfaces.api.members.views import (
    MemberRegisterView,
    MemberValidateView,
    MemberActivateView,
)

urlpatterns = [
    path("", MemberRegisterView.as_view()),
    path("<uuid:member_id>/validate/", MemberValidateView.as_view()),
    path("<uuid:member_id>/activate/", MemberActivateView.as_view()),
]