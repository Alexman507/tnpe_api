from django.test import TestCase
from ..models import Supplier

class SupplierTestCase(TestCase):
    def setUp(self):
        self.parent_supplier = Supplier.objects.create(name='Родительский поставщик')
        self.child_supplier = Supplier.objects.create(name='Дочерний поставщик', parent=self.parent_supplier)
        self.grandchild_supplier = Supplier.objects.create(name='Внучатый поставщик', parent=self.child_supplier)

    def test_set_level(self):
        # Сохраняем поставщиков, чтобы вызвать сигнал pre_save
        self.parent_supplier.save()
        self.child_supplier.save()
        self.grandchild_supplier.save()

        # Проверяем, что уровень поставщиков установлен правильно
        self.assertEqual(self.parent_supplier.level, 0)
        self.assertEqual(self.child_supplier.level, 1)
        self.assertEqual(self.grandchild_supplier.level, 2)
