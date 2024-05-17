from django import forms
from .models import LoanApplication, Payment

# Create Forms 
class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ('amount', 'purpose', )


class MakePaymentsForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount']