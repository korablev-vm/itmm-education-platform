from django.contrib import admin
from .models import Token

@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')
    search_fields = ('user__username',)
    list_editable = ('amount',)