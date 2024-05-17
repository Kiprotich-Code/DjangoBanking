from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction

# Signal handler to update balance after each transaction
@receiver(post_save, sender=Transaction)
def update_balance(sender, instance, created, **kwargs):
    if created:
        instance.account.balance += instance.amount
        instance.account.save()