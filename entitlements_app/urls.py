from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntitlementViewSet

router = DefaultRouter()
router.register(r'entitlements', EntitlementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]