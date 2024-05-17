from django.shortcuts import render
from django.views.generic import ListView, DetailView
from main.models import Account

# Create your views here.
def dashboard(request):
    return render(request, 'admins/dashboard.html')


# ACCOUNTS 
class AccountsListView(ListView):
    context_object_name = 'accounts'
    model = Account
    template_name = 'admins/accounts.html'
    paginate_by = 5
    ordering = '-date_of_creation'


class AccountDetailView(DetailView):
    context_object_name = 'account'
    model = Account
    template_name = 'admins/account_details.html'