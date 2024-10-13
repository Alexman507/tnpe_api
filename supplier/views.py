from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from users.permissions import IsActiveEmployeePermission
from .serializers import FactorySerializer, RetailNetworkSerializer, IndividualEntrepreneurSerializer, \
    SupplierSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(operation_description="Список поставщиков")
)
class SupplierViewSet(viewsets.ModelViewSet):
    """
    API для управления поставщиками.
    Поддерживает методы GET, POST, PUT, DELETE.
    """

    serializer_class = SupplierSerializer
    permission_classes = [IsActiveEmployeePermission]
    read_only_fields = ('debt',)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']

    def get_queryset(self):
        return self.model.objects.all()

    def get_serializer_class(self):
        return self.serializer_class

    def update(self, request, *args, **kwargs):
        if 'debt' in request.data:
            request.data.pop('debt')
        return super().update(request, *args, **kwargs)

class FactoryViewSet(SupplierViewSet):
    """
    API для управления фабриками.
    """
    serializer_class = FactorySerializer

class RetailNetworkViewSet(SupplierViewSet):
    """
    API для управления розничными сетями.
    """
    serializer_class = RetailNetworkSerializer

class IndividualEntrepreneurViewSet(SupplierViewSet):
    """
    API для управления индивидуальными предпринимателями.
    """
    serializer_class = IndividualEntrepreneurSerializer
