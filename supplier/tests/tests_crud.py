from rest_framework.test import APITestCase
from rest_framework import status
from supplier.models import Supplier, Factory, RetailNetwork, IndividualEntrepreneur

from users.models import User


class SupplierAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.supplier = Supplier.objects.create(name="Test Supplier")
        self.factory = Factory.objects.create(
            name="Test Factory", supplier=self.supplier
        )
        self.retail_network = RetailNetwork.objects.create(
            name="Test Retail Network", supplier=self.supplier
        )
        self.individual_entrepreneur = IndividualEntrepreneur.objects.create(
            name="Test Individual Entrepreneur", supplier=self.supplier
        )

    def test_get_suppliers(self):
        response = self.client.get("/suppliers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_supplier(self):
        response = self.client.get(f"/suppliers/{self.supplier.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Supplier")

    def test_create_supplier(self):
        data = {"name": "New Supplier"}
        response = self.client.post("/suppliers/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 2)

    def test_update_supplier(self):
        data = {"name": "Updated Supplier"}
        response = self.client.put(f"/suppliers/{self.supplier.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Supplier.objects.get(id=self.supplier.id).name, "Updated Supplier"
        )

    def test_delete_supplier(self):
        response = self.client.delete(f"/suppliers/{self.supplier.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Supplier.objects.count(), 0)


class FactoryAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.supplier = Supplier.objects.create(name="Test Supplier")
        self.factory = Factory.objects.create(
            name="Test Factory", supplier=self.supplier
        )

    def test_get_factories(self):
        response = self.client.get("/factories/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_factory(self):
        response = self.client.get(f"/factories/{self.factory.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Factory")

    def test_create_factory(self):
        data = {"name": "New Factory", "supplier": self.supplier.id}
        response = self.client.post("/factories/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Factory.objects.count(), 2)

    def test_update_factory(self):
        data = {"name": "Updated Factory"}
        response = self.client.put(f"/factories/{self.factory.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Factory.objects.get(id=self.factory.id).name, "Updated Factory"
        )

    def test_delete_factory(self):
        response = self.client.delete(f"/factories/{self.factory.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Factory.objects.count(), 0)


class RetailNetworkAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.supplier = Supplier.objects.create(name="Test Supplier")
        self.retail_network = RetailNetwork.objects.create(
            name="Test Retail Network", supplier=self.supplier
        )

    def test_get_retail_networks(self):
        response = self.client.get("/retail-networks/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_retail_network(self):
        response = self.client.get(f"/retail-networks/{self.retail_network.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Retail Network")

    def test_create_retail_network(self):
        data = {"name": "New Retail Network", "supplier": self.supplier.id}
        response = self.client.post("/retail-networks/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RetailNetwork.objects.count(), 2)

    def test_update_retail_network(self):
        data = {"name": "Updated Retail Network"}
        response = self.client.put(f"/retail-networks/{self.retail_network.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            RetailNetwork.objects.get(id=self.retail_network.id).name,
            "Updated Retail Network",
        )

    def test_delete_retail_network(self):
        response = self.client.delete(f"/retail-networks/{self.retail_network.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(RetailNetwork.objects.count(), 0)


class IndividualEntrepreneurAPITestCase(APITestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name="Test Supplier")
        self.individual_entrepreneur = IndividualEntrepreneur.objects.create(
            name="Test Individual Entrepreneur", supplier=self.supplier
        )

    def test_get_individual_entrepreneurs(self):
        response = self.client.get("/individual-entrepreneurs/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_individual_entrepreneur(self):
        response = self.client.get(
            f"/individual-entrepreneurs/{self.individual_entrepreneur.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Individual Entrepreneur")

    def test_create_individual_entrepreneur(self):
        data = {"name": "New Individual Entrepreneur", "supplier": self.supplier.id}
        response = self.client.post("/individual-entrepreneurs/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(IndividualEntrepreneur.objects.count(), 2)

    def test_update_individual_entrepreneur(self):
        data = {"name": "Updated Individual Entrepreneur"}
        response = self.client.put(
            f"/individual-entrepreneurs/{self.individual_entrepreneur.id}/", data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            IndividualEntrepreneur.objects.get(id=self.individual_entrepreneur.id).name,
            "Updated Individual Entrepreneur",
        )

    def test_delete_individual_entrepreneur(self):
        response = self.client.delete(
            f"/individual-entrepreneurs/{self.individual_entrepreneur.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(IndividualEntrepreneur.objects.count(), 0)
