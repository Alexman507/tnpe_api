from rest_framework import serializers
from .models import Factory, RetailNetwork, IndividualEntrepreneur, Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """
    Сериализатор для поставщиков.
    """
    class Meta:
        model = Supplier
        fields = '__all__'

class FactorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для заводов.
    """
    class Meta:
        model = Factory
        fields = '__all__'

class RetailNetworkSerializer(serializers.ModelSerializer):
    """
    Сериализатор для розничных сетей.
    """
    class Meta:
        model = RetailNetwork
        fields = '__all__'

class IndividualEntrepreneurSerializer(serializers.ModelSerializer):
    """
    Сериализатор для индивидуальных предпринимателей.
    """
    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'