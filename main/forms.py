from django import forms
from .models import Account, Transaction

# Forms 
class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('account_type', 'account_no', )

class DepositForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('account', 'desc', 'amount', )


class TransferForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('account', 'destination_acc', 'desc', 'amount', )