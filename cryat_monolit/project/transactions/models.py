import uuid
from django.db import models
from usermanage.models import User

class Wallet_FIAT(models.Model):
    wallet = (
        ('fiat', 'FIAT account'),
        ('saving', 'Saving account'),
    )
    currency = (
        ('usd', 'USD'),
        ('rub', 'RUB'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wallets')
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    wallet_type = models.CharField(max_length=10, choices=wallet)
    currency = models.CharField(max_length=3, choices=currency)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    

    class Meta:
        db_table = 'wallets'
        verbose_name = 'Кошелёк'
        verbose_name_plural = 'Кошельки'

    def __str__(self):
        return f"Wallet of {self.user.nickname}"


class Transaction(models.Model):
    trans_types = (
        ('transfer', 'Transfer'),
        ('between', 'Between'),
    )
    trans_state = (
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    sender = models.ForeignKey(Wallet_FIAT, on_delete=models.CASCADE, related_name='sent_transactions', primary_key=False)
    receiver = models.ForeignKey(Wallet_FIAT, on_delete=models.CASCADE, related_name='received_transactions', primary_key=False)
    transaction_type = models.CharField(max_length=15, choices=trans_types)
    transaction_state = models.CharField(max_length=15, choices=trans_state, default='completed')
    currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transaction'
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    def __str__(self):
        return f"{self.transaction_type} {self.amount} {self.currency}"