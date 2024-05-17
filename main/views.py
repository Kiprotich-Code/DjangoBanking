from django.shortcuts import render, redirect
from .forms import CreateAccountForm, DepositForm, TransferForm
from .models import Account, Transaction

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'main/home.html')


# User Views 
# Accounts
def accounts(request):
    accounts = Account.objects.filter(user=request.user)
    context = {
        'accounts': accounts
    }
    return render(request, 'main/accounts.html', context)

def acc_details(request, id):
    account = Account.objects.filter(id=id)
    context = {
        'account': account
    }
    return render(request, 'main/account_details.html', context)

# Create Account 
def add_account(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            acc = form.save(commit=False)
            acc.user = request.user
            acc.balance = 0
            acc.save()
            return redirect('accounts')

    else:
        form = CreateAccountForm()

    return render(request, 'main/add_account.html', {'form': form})
            

# Transactions 
# Deposit 
def deposit_funds(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            amount = form.cleaned_data['amount']

            transaction = Transaction.objects.create(account=account, amount=amount)
            return redirect('accounts')
    else:
        form = DepositForm()
    
    context = {
        'form': form,
    }
    return render(request, 'main/deposit.html', context)


# send 

