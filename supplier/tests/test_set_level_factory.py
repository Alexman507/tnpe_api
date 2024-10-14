from django.test import TestCase
from ..models import Factory

class FactoryTestCase(TestCase):
    def setUp(self):
        self.parent_factory = Factory.objects.create(name='Родительский завод')
        self.child_factory = Factory.objects.create(name='Дочерний завод', parent=self.parent_factory)
        self.grandchild_factory = Factory.objects.create(name='Внучатый завод', parent=self.child_factory)

    def test_set_level(self):
        # Сохраняем заводы, чтобы вызвать сигнал pre_save
        self.parent_factory.save()
        self.child_factory.save()
        self.grandchild_factory.save()

        # Проверяем, что уровень заводов установлен правильно
        self.assertEqual(self.parent_factory.level, 0)
        self.assertEqual(self.child_factory.level, 1)
        self.assertEqual(self.grandchild_factory.level, 2)

