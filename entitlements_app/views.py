from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Entitlement
from .serializers import EntitlementSerializer

def get_user_entitlements(user):
    active_entitlements = [e for e in user.entitlements.all() if e.is_active()]
    merged = set()
    for ent in active_entitlements:
        merged.update(ent.entitlements())
    return list(merged)

class EntitlementViewSet(viewsets.ModelViewSet):
    queryset = Entitlement.objects.all()
    serializer_class = EntitlementSerializer

    @action(detail=False, methods=["get"], url_path="user/(?P<user_id>[^/.]+)/current")
    def current_entitlements(self, request, user_id=None):
        user = User.objects.get(pk=user_id)
        entitlements = get_user_entitlements(user)
        return Response({"entitlements": entitlements})