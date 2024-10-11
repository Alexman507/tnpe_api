from django.contrib import admin
from .models import Supplier, Factory, RetailNetwork, IndividualEntrepreneur

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'debt', 'supplier')
    list_filter = ('name', "contacts.city")
    actions = ['clear_debt']
    def clear_debt(self, request, queryset):
        for obj in queryset:
            obj.debt = 0
            obj.save()

    clear_debt.short_description = 'Очистить задолженность'

class FactoryAdmin(SupplierAdmin):
    pass

class RetailNetworkAdmin(SupplierAdmin):
    pass

class IndividualEntrepreneurAdmin(SupplierAdmin):
    pass

admin.site.register(Factory, FactoryAdmin)
admin.site.register(RetailNetwork, RetailNetworkAdmin)
admin.site.register(IndividualEntrepreneur, IndividualEntrepreneurAdmin)
