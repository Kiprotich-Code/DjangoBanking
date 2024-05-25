from django.db import models
from users.models import CustomUser
from django.utils.crypto import get_random_string

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, choices=[
        ('current', 'Current'),
        ('savings', 'Savings'),
        ('fixedDeposit', 'FixedDeposit'),
        ('salary', 'Salary'),
        ('mmas', 'MMAs'),
    ], default='Savings')
    account_no = models.CharField(max_length=100, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending')
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user.email}, created a {self.account_type} account.'
    
    def save(self, *args, **kwargs):
        if not self.account_no:
            self.account_no = self.generate_account_no()
        super().save(*args, **kwargs)

    def generate_account_no(self):
        prefix = 'ACC'
        unique_no = get_random_string(length=10, allowed_chars='0123456789')
        return f'{prefix}{unique_no}'

class Transaction(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.CharField(max_length=100, blank=True)
    destination_acc = models.ManyToManyField(Account, related_name="destination_account", blank=True)

    def __str__(self):
        return f'{self.account} - {self.transaction_type}'
    