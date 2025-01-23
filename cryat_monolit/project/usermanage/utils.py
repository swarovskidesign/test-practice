import random
import string
from .models import User

def generate_unique_key():
    while True:
        result = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%?*/", k=32))
        if not User.objects.filter(unique_key=result).exists():
            return result