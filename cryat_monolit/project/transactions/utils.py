from django.http import JsonResponse
from decimal import Decimal, InvalidOperation

def is_valid_value(amount):
    try:
        return Decimal(amount)
    except (ValueError, InvalidOperation):
        return JsonResponse({'message': 'enter the correct value'})