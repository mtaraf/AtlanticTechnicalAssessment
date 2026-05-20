from rest_framework import serializers
from .models import Entitlement

class EntitlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entitlement
        fields = ['id', 'user', 'product', 'start_date', 'end_date', 'revoked']