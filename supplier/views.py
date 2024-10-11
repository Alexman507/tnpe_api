from rest_framework import viewsets
from .models import Factory, RetailNetwork, IndividualEntrepreneur
from .serializers import FactorySerializer, RetailNetworkSerializer, IndividualEntrepreneurSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    read_only_fields = ('debt',)

    def get_queryset(self):
        return self.model.objects.all()

    def get_serializer_class(self):
        return self.serializer_class

    def update(self, request, *args, **kwargs):
        if 'debt' in request.data:
            request.data.pop('debt')
        return super().update(request, *args, **kwargs)

class FactoryViewSet(SupplierViewSet):
    model = Factory
    serializer_class = FactorySerializer

class RetailNetworkViewSet(SupplierViewSet):
    model = RetailNetwork
    serializer_class = RetailNetworkSerializer

class IndividualEntrepreneurViewSet(SupplierViewSet):
    model = IndividualEntrepreneur
    serializer_class = IndividualEntrepreneurSerializer
