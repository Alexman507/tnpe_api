from django.test import TestCase
from ..models import RetailNetwork

class RetailNetworkTestCase(TestCase):
    def setUp(self):
        self.parent_retail_network = RetailNetwork.objects.create(name='Родительская розничная сеть')
        self.child_retail_network = RetailNetwork.objects.create(name='Дочерняя розничная сеть', parent=self.parent_retail_network)
        self.grandchild_retail_network = RetailNetwork.objects.create(name='Внучатая розничная сеть', parent=self.child_retail_network)

    def test_set_level(self):
        # Сохраняем розничные сети, чтобы вызвать сигнал pre_save
        self.parent_retail_network.save()
        self.child_retail_network.save()
        self.grandchild_retail_network.save()

        # Проверяем, что уровень розничных сетей установлен правильно
        self.assertEqual(self.parent_retail_network.level, 0)
        self.assertEqual(self.child_retail_network.level, 1)
        self.assertEqual(self.grandchild_retail_network.level, 2)
