from django.urls import include, path
from rest_framework import routers

from supplier.apps import SupplierConfig
from supplier.views import (
    IndividualEntrepreneurViewSet,
    FactoryViewSet,
    RetailNetworkViewSet,
    SupplierViewSet,
)


app_name = SupplierConfig.name

router = routers.DefaultRouter()
# Registering the viewsets with the router to include them in the API
router.register(r"supplier", SupplierViewSet, basename="suppliers")
router.register(r"factories", FactoryViewSet, basename="factories")
router.register(r"retail", RetailNetworkViewSet, basename="retail")
router.register(r"individual", IndividualEntrepreneurViewSet, basename="individual")

urlpatterns = [
    path("", include(router.urls)),
]
