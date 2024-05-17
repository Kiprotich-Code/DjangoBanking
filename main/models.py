from django.db import models
from users.models import CustomUser

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=100)
    account_no = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user.email}, created a {self.account_type} account.'
    

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.CharField(max_length=100, blank=True)
    destination_acc = models.ManyToManyField(Account, related_name="destination_account", blank=True)

    def __str__(self):
        return f'{self.account} - {self.transaction_type}'
    