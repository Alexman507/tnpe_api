from rest_framework import serializers
from .models import Factory, RetailNetwork, IndividualEntrepreneur, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'

class RetailNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailNetwork
        fields = '__all__'

class IndividualEntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'