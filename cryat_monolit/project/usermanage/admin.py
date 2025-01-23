from django.contrib import admin
from .models import User
from transactions.admin import WalletTabAdmin

@admin.register(User)
class UserAdminPanel(admin.ModelAdmin):
    list_display = ['nickname', 'password', 'favorite_word', 'role']
    list_editable = ['favorite_word', 'role']
    search_fields = ['nickname', 'role']

    inlines = [WalletTabAdmin]