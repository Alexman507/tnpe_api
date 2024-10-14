from django.contrib import admin
from .models import Supplier, Factory, RetailNetwork, IndividualEntrepreneur, Product, Contacts


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'debt', 'parent', 'level')
    list_filter = ('name', "contacts__city")
    actions = ['clear_debt']
    def clear_debt(self, request, queryset):
        for obj in queryset:
            obj.debt = 0
            obj.save()

    clear_debt.short_description = 'Очистить задолженность'

@admin.register(Factory)
class FactoryAdmin(SupplierAdmin):
    pass

@admin.register(RetailNetwork)
class RetailNetworkAdmin(SupplierAdmin):
    pass

@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(SupplierAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'house_number')
