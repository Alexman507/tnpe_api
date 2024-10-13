# Электронная сеть по продаже электроники

Проект представляет собой веб-приложение с API-интерфейсом и админ-панелью, созданное на основе Django и Django Rest Framework.

## Основная функциональность

* Реализация модели сети по продаже электроники с иерархической структурой из трех уровней: завод, розничная сеть, индивидуальный предприниматель.
* Каждое звено сети имеет название, контакты, продукты, поставщика и задолженность перед поставщиком.
* Админ-панель для создания и управления объектами сети.
* API для CRUD операций с моделью поставщика, с возможностью фильтрации объектов по определенной стране.
* Права доступа к API ограничены только активными сотрудниками.

## Технологии и библиотеки

* Python 3.12
* Django 3+
* Django Rest Framework 3.10+
* PostgreSQL 10+

## Установка и запуск

* Клонировать репозиторий
* Установить зависимости с помощью `pip install -r requirements.txt`
* Создать базу данных с помощью `python manage.py migrate`
* Запустить сервер с помощью `python manage.py runserver`

## API

* CRUD операции с моделью поставщика: `api/suppliers/`
* Фильтрация объектов по определенной стране: `api/suppliers/?country=<country_name>`

## Админ-панель

* Создание и управление объектами сети: `admin/suppliers/`
* Ссылка на поставщика: `admin/suppliers/<supplier_id>/`
* Фильтр по названию города: `admin/suppliers/?city=<city_name>`
* Admin action для очистки задолженности перед поставщиком: `admin/suppliers/<supplier_id>/clear_debt/`

## Авторы

* [Ваше имя]

## Лицензия

* MIT License
#TODO:

Если исключить из списка CRUD (Create, Read, Update, Delete) и метод `set_level`, то останется:

1. **Валидация моделей**: можно написать тесты для проверки валидации моделей, например, проверять, что модель сохраняется только при правильных данных.
2. **Работа с формами**: можно написать тесты для проверки работы с формами, например, проверять, что формы валидируются правильно.
3. **Работа с API**: можно написать тесты для проверки работы с API, например, проверять, что API возвращает правильные данные.
4. **Авторизация и аутентификация**: можно написать тесты для проверки авторизации и аутентификации, например, проверять, что пользователь авторизуется и аутентифицируется правильно.
5. **Работа с файлами**: можно написать тесты для проверки работы с файлами, например, проверять, что файлы загружаются и скачиваются правильно.

Эти тесты будут проверять функциональность, которая не связана напрямую с CRUD-операциями и методом `set_level`.