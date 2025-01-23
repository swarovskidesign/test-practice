from django.urls import path
from .views import SendTransactions, CreateWallet, BetweenTransactions, Exchange

app_name = 'wallets'

urlpatterns = [
    path('send/', SendTransactions.as_view(), name = 'send_transaction'),
    path('between/', BetweenTransactions.as_view(), name = 'between_transaction'),
    path('exchange/', Exchange.as_view(), name = 'exchange_amount'),
    path('createwallet/', CreateWallet.as_view(), name = 'createwallet')
]
