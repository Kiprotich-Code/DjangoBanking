from django.contrib import admin
from .models import LoanApplication, Loan, Payment

# Register your models here.
admin.site.register(LoanApplication)
admin.site.register(Loan)
admin.site.register(Payment)