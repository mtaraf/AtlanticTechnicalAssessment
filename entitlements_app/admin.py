from django.contrib import admin
from .models import Entitlement

@admin.register(Entitlement)
class EntitlementAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'start_date', 'end_date', 'revoked', 'is_active']
    list_filter = ['product', 'revoked']