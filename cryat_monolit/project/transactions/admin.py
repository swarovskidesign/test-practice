from django.contrib import admin
from .models import Wallet_FIAT, Transaction

class WalletTabAdmin(admin.TabularInline):
    model = Wallet_FIAT
    fields = ['token', 'wallet_type', 'currency', 'balance']
    search_fields = ['token', 'currency', 'balance']
    readonly_fields = ['token', 'wallet_type', 'currency', 'balance']
    extra = 1

@admin.register(Wallet_FIAT)
class Wallet_FIATAdmin(admin.ModelAdmin):
    list_display = ['user', 'token', 'wallet_type', 'currency', 'balance']
    list_editable = ['balance']
    search_fields = ['user', 'token', 'wallet_type']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'transaction_state', 'amount', 'date']
    list_editable = ['transaction_state']
    search_fields = ['sender', 'receiver', 'transaction_state']
    list_filter = ['transaction_state', 'date']