from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime

NULLABLE = {'null': True, 'blank': True}

class Contacts(models.Model):
    email = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}, {self.house_number}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.model})"

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, related_name='children')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Supplier)
def set_level(sender, instance, **kwargs):
    if instance.supplier:
        instance.level = instance.supplier.level + 1
    else:
        instance.level = 0

class Factory(Supplier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class RetailNetwork(Supplier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class IndividualEntrepreneur(Supplier):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)