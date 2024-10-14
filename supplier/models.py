from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

NULLABLE = {"null": True, "blank": True}


class Contacts(models.Model):
    """
    Модель контактов.
    Хранит информацию о контактах поставщика.
    """

    email = models.EmailField(max_length=50, verbose_name="Электронная почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}, {self.house_number}"

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class Product(models.Model):
    """
    Модель продукта.
    Хранит информацию о продуктах, которые поставляет поставщик.
    """

    name = models.CharField(max_length=100, verbose_name="Название")
    model = models.CharField(max_length=100, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Supplier(models.Model):
    """
    Модель поставщика.
    Хранит информацию о поставщике и его контактах.
    Описана не абстрактно на случай, если поставщик не может быть отнесён к классам потомков.
    """

    name = models.CharField(max_length=100)
    contacts = models.OneToOneField(
        Contacts,
        on_delete=models.CASCADE,
        **NULLABLE,
        related_name="supplier_contacts",
        verbose_name="Контакты",
    )
    products = models.ManyToManyField(
        Product, verbose_name="Продукты", blank=True, related_name="supplier_products"
    )
    parent = models.ForeignKey("self", on_delete=models.CASCADE, **NULLABLE, verbose_name="Поставщик")
    debt = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Задолженность (руб.)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def save(self, *args, **kwargs):
        if self.parent:
            self.level = self.parent.level + 1
        else:
            self.level = 0
        super().save(*args, **kwargs)


class Factory(Supplier):
    """
    Модель завода.
    Наследует все поля и методы модели Supplier.
    """

    def __str__(self):
        return f"Завод: {self.name}"

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"


class RetailNetwork(Supplier):
    """
    Модель розничной сети.
    Наследует все поля и методы модели Supplier.
    """

    def __str__(self):
        return f"Розничная сеть: {self.name}"

    class Meta:
        verbose_name = "Розничная сеть"
        verbose_name_plural = "Розничные сети"


class IndividualEntrepreneur(Supplier):
    """
    Модель индивидуального предприятия.
    Наследует все поля и методы модели Supplier.
    """

    def __str__(self):
        return f"Индивидуальное предприятие: {self.name}"

    class Meta:
        verbose_name = "Индивидуальное предприятие"
        verbose_name_plural = "Индивидуальные предприятия"
