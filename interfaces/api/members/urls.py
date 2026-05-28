# interfaces/api/members/urls.py

from django.urls import path
from .views import RegisterMemberUseCaseView, ActivateMemberUseCaseView

urlpatterns = [
    path('register/', RegisterMemberUseCaseView.as_view(), name='register-member'),
    path('activate/', ActivateMemberUseCaseView.as_view(), name='activate-member'),
]