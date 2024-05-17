from django.urls import path
from . import views

urlpatterns = [
    path('', views.loans, name="loans"),
    path('loan_application', views.loan_application, name="loan_application"),
    path('make_payment/<int:loan_id>', views.make_payment, name='make_payment'),
]