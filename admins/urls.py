from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('manage_accounts/', login_required(views.AccountsListView.as_view()), name="manage_accounts"),
    path('admins_accounts_details/<pk>', login_required(views.AccountDetailView.as_view()), name="admins_account_details"),
    path('accounts/<int:account_id>/approve/', views.approve_account, name='approve_account'),
    path('accounts/<int:account_id>/reject/', views.reject_account, name='reject_account'),
]