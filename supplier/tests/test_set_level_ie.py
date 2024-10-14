from django.test import TestCase
from ..models import IndividualEntrepreneur

class IndividualEntrepreneurTestCase(TestCase):
    def setUp(self):
        self.parent_individual_entrepreneur = IndividualEntrepreneur.objects.create(name='Родительский индивидуальный предприниматель')
        self.child_individual_entrepreneur = IndividualEntrepreneur.objects.create(name='Дочерний индивидуальный предприниматель', parent=self.parent_individual_entrepreneur)
        self.grandchild_individual_entrepreneur = IndividualEntrepreneur.objects.create(name='Внучатый индивидуальный предприниматель', parent=self.child_individual_entrepreneur)

    def test_set_level(self):
        # Сохраняем индивидуальных предпринимателей, чтобы вызвать сигнал pre_save
        self.parent_individual_entrepreneur.save()
        self.child_individual_entrepreneur.save()
        self.grandchild_individual_entrepreneur.save()

        # Проверяем, что уровень индивидуальных предпринимателей установлен правильно
        self.assertEqual(self.parent_individual_entrepreneur.level, 0)
        self.assertEqual(self.child_individual_entrepreneur.level, 1)
        self.assertEqual(self.grandchild_individual_entrepreneur.level, 2)