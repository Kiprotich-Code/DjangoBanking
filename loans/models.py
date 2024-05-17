from django.db import models
from django.conf import settings

# Create your models here.
# Loan Application 
class LoanApplication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='pending')
    application_date = models.DateTimeField(auto_now_add=True)
    approval_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.user.email} - {self.amount} - {self.status}'
    
# Loan if an application is approved 
class Loan(models.Model):
    application = models.OneToOneField(LoanApplication, on_delete=models.CASCADE)
    approved_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return f"Loan for {self.application.user.email} - {self.approved_amount}"
    

class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Payment of {self.amount} on {self.payment_date}'