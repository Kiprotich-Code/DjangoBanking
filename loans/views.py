from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoanApplicationForm, MakePaymentsForm
from .models import LoanApplication, Loan

# Create your views here.
# Apply for a loan 
def loan_application(request):
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.user = request.user
            loan.save()
            return redirect('loans')
    else:
        form = LoanApplicationForm()

    context = {
        'form': form
    }
    return render(request, 'loans/loan_application.html', context)


# All loans 
def loans(request):
    all_loans = LoanApplication.objects.filter(user=request.user)
    context = {
        'all_loans': all_loans
    }
    return render(request, 'loans/loans.html', context)


# Make Payments 
def make_payment(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id)

    if request.method == 'POST':
        form = MakePaymentsForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.loan = loan
            payment.save()
            return redirect('loans')
        
    else:
        form = MakePaymentsForm()
    context = {
        'form': form,
        'loan': loan
    }
    return render(request, 'loans/make_payment.html', context)