from django.urls import include, path
from rest_framework import routers

from supplier.views import (
    IndividualEntrepreneurViewSet,
    FactoryViewSet,
    RetailNetworkViewSet,
    SupplierViewSet,
)

router = routers.DefaultRouter()
# Registering the viewsets with the router to include them in the API
router.register(r"suppliers", SupplierViewSet)
router.register(r"factories", FactoryViewSet)
router.register(r"retail", RetailNetworkViewSet)
router.register(r"individual", IndividualEntrepreneurViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
