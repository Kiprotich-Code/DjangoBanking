from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),

    # accounts 
    path('accounts/', views.accounts, name="accounts"),
    path('add_account/', views.add_account, name="add_account"),
    path('account_details/<int:id>', views.acc_details, name="account_details"),

    # Transactions 
    path('deposit/', views.deposit_funds, name="deposit"),
]