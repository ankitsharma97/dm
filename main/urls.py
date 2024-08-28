from django.urls import path
from .views import BranchSearchAPIView, BankListAPIView

urlpatterns = [
    path('banks/', BankListAPIView.as_view(), name='bank-list'),
    path('branch-search/', BranchSearchAPIView.as_view(), name='branch-search'),
]
