from django.http import JsonResponse
from django.views import View
from django.db import transaction
from django.utils.timezone import now
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from .models import Wallet_FIAT as wlt, Transaction as trans
from .utils import is_valid_value

valid_wallet_types = ["fiat", "saving"]
valid_currencies = ["usd", "rub"]


class SendTransactions(View):
    def post(self, request):
        try:
            token_rec = request.POST.get("token")
            currency = request.POST.get("currency")
            amount = request.POST.get("count")

            count = is_valid_value(amount)
            if isinstance(count, JsonResponse):
                return count

            sender = wlt.objects.filter(
                user=request.user, wallet_type="fiat", currency=currency
            ).first()

            if not sender:
                return JsonResponse({"message": "sender wallet not found"}, status=400)

            if sender.balance < count:
                return JsonResponse({"message": "invalid balance"}, status=400)

            reciever = wlt.objects.filter(
                token=token_rec, wallet_type="fiat", currency=currency
            ).first()

            if not reciever:
                return JsonResponse({"message": "receiver wallet not found"}, status=400)

            with transaction.atomic():
                sender.balance -= count
                reciever.balance += count
                sender.save()
                reciever.save()

                trans.objects.create(
                    sender=sender,
                    receiver=reciever,
                    transaction_type="transfer",
                    currency=currency,
                    amount=count,
                    date=now(),
                )

                return JsonResponse({"message": "completed"}, status=200)

        except Exception as e:
            sender_token = sender.token if 'sender' in locals() and sender else None
            receiver_token = reciever.token if 'reciever' in locals() and reciever else None

            trans.objects.create(
                sender=sender_token,
                receiver=receiver_token,
                transaction_type="transfer",
                transaction_state="failed",
                currency=currency,
                amount=count if 'count' in locals() else None,
                date=now(),
            )
            return JsonResponse(
                {"message": "transaction failed", "error": str(e)}, status=500
            )


class BetweenTransactions(View):
    def post(self, request):
        try:
            wlt_type = request.POST.get("wallet_type")
            amount = request.POST.get("amount")
            currency = request.POST.get("currency")

            count = is_valid_value(amount)
            if isinstance(count, JsonResponse):
                return count
            
            global valid_wallet_types
            type_for_between = (
                valid_wallet_types[1]
                if currency == valid_wallet_types[0]
                else valid_wallet_types[0]
            )

            with transaction.atomic():
                sender = wlt.objects.filter(user=request.user, wallet_type=type_for_between, currency=currency).first()
                receiver = wlt.objects.filter(user=request.user, wallet_type=wlt_type, currency=currency).first()
                

                if sender.balance < count:
                    return JsonResponse({"message": "invalid balance"})

                sender.balance -= count
                receiver.balance += count

                sender.save()
                receiver.save()

                trans.objects.create(
                    sender=sender,
                    receiver=receiver,
                    transaction_type="between",
                    transaction_state="completed",
                    currency=currency,
                    amount=count,
                    date=now(),
                )

                return JsonResponse({"message": "transaction successful"}, status=200)

        except Exception as e:
            trans.objects.create(
                sender = sender.token,
                receiver = receiver.token,
                transaction_type = 'between',
                transaction_state = 'failed',
                currency = currency,
                amount = count,
                date=now()
            )
            return JsonResponse({"message": "transaction failed"}, status=500)

class Exchange(View):
    def post(self, request):
        currency = request.POST.get("currency")
        amount = request.POST.get("amount")

        if not all([currency, amount]):
            return JsonResponse(
                {"message": "missing parameters: currency or amount"}, status=400
            )

        count = is_valid_value(amount)
        if isinstance(count, JsonResponse):
            return count

        global valid_currencies
        currency_for_between = (
            valid_currencies[1]
            if currency == valid_currencies[0]
            else valid_currencies[0]
        )

        with transaction.atomic():
            wallet_from = wlt.objects.filter(
                user=request.user, wallet_type="fiat", currency=currency
            ).first()
            wallet_to = wlt.objects.filter(
                user=request.user, wallet_type="fiat", currency=currency_for_between
            ).first()

            if not wallet_from or not wallet_to:
                return JsonResponse({"message": "wallets not found"}, status=400)

            if currency_for_between == "rub":
                count = Decimal(amount) / 100
            else:
                count = Decimal(amount) * 100

            if count <= 0:
                return JsonResponse({"message": "invalid value"}, status=400)

            if wallet_from.balance < count:
                return JsonResponse({"message": "insufficient balance"}, status=400)

            wallet_from.balance -= count
            wallet_to.balance += Decimal(amount)

            wallet_from.save()
            wallet_to.save()

            trans.objects.create(
                sender=wallet_from,
                receiver=wallet_to,
                transaction_type="between",
                transaction_state="completed",
                currency=currency,
                amount=Decimal(amount),
                date=now(),
            )

            return JsonResponse({"message": "exchange successful"}, status=200)


class CreateWallet(View):
    def post(self, request):
        wallet_type = request.POST.get("wallet_type")
        currency = request.POST.get("currency")

        global valid_wallet_types
        global valid_currencies

        with transaction.atomic():
            if wlt.objects.filter(
                user=request.user, wallet_type=wallet_type, currency=currency
            ).exists():
                return JsonResponse(
                    {"message": "u already have this wallet"}, status=400
                )

            if (
                wallet_type not in valid_wallet_types
                or currency not in valid_currencies
            ):
                return JsonResponse(
                    {"message": "Invalid wallet_type or currency"}, status=400
                )

            wlt.objects.create(
                user=request.user, wallet_type=wallet_type, currency=currency
            )
            return JsonResponse({"message": "wallets created successfuly"})
