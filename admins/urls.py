from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('manage_accounts/', views.AccountsListView.as_view(), name="manage_accounts"),
    path('admins_accounts_details/<pk>', views.AccountDetailView.as_view(), name="admins_account_details"),
]