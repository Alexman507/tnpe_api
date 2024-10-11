from django.urls import include, path
from rest_framework import routers

from supplier.views import IndividualEntrepreneurViewSet, FactoryViewSet, RetailNetworkViewSet

router = routers.DefaultRouter()
router.register(r'factories', FactoryViewSet)
router.register(r'retail', RetailNetworkViewSet)
router.register(r'individual', IndividualEntrepreneurViewSet)

urlpatterns = [
    path('', include(router.urls)),
]