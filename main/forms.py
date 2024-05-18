from django import forms
from .models import Account, Transaction

# Forms 
class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('account_type', )

class DepositForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('desc', 'amount', )


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('account', 'destination_acc', 'desc', 'amount', )