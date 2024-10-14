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
* Django 4.2.14
* Django Rest Framework 3.15.2
* PostgreSQL 16.0

### Сторонние библиотеки

* Pillow 10.4.0
* Black 24.10.0
* Django Stubs 5.0.4
* Django Filter 24.3
* Coverage 7.6.1
* Django Dispatch 1.0.1
* Requests 2.32.3
* drf-yasg~=1.21.7
* dj-rest-auth~=5.0.1 (https://dj-rest-auth.readthedocs.io/en/latest/installation.html)
* django-allauth~=65.0.2

## Установка и запуск

* Клонировать репозиторий
* Установить зависимости с помощью `pip install -r requirements.txt`
* Заполнить в .env переменные с помощью файла .env.example
* Создать БД в СУБД PostgreSQL, если postgres уже используется
* Создать базу данных с помощью `python manage.py migrate`
* Запустить сервер с помощью `python manage.py runserver`

## API
* Автодокументация: `/redoc/` и `/swagger/`
* CRUD операции с моделью поставщика: `/supplier/suppliers/`
* Модель завода: `/supplier/factories/`
* Модель розничной сети: `/supplier/retail`
* Модель индивидуального предпринимателя: `/supplier/individual/`
* Фильтрация объектов по определенной стране: `/suppliers/?country=<country_name>`

## Админ-панель
Проще работать через 
* Создание и управление объектами сети: `admin/supplier/<суффикс поставщика>/`
* Ссылка на поставщика: `admin/supplier/<суффикс поставщика>/<supplier_id>/`
* Фильтр по названию города: `admin/supplier/<суффикс поставщика>/?city=<city_name>`
* Admin action для очистки задолженности перед поставщиком: `admin/suppliers/<суффикс поставщика>/<supplier_id>/clear_debt/`

## Авторы

* Алексей Алексуткин (https://t.me/AlexNeroEUC, https://github.com/Alexman507)


# TODO:
Покрытие тестами (оставшееся):
1. **Валидация моделей**: можно написать тесты для проверки валидации моделей, например, проверять, что модель сохраняется только при правильных данных.
2. **Работа с формами**: можно написать тесты для проверки работы с формами, например, проверять, что формы валидируются правильно.
3. **Работа с API**: можно написать тесты для проверки работы с API, например, проверять, что API возвращает правильные данные.
4. **Авторизация и аутентификация**: можно написать тесты для проверки авторизации и аутентификации, например, проверять, что пользователь авторизуется и аутентифицируется правильно.
5. **Работа с файлами**: можно написать тесты для проверки работы с файлами, например, проверять, что файлы загружаются и скачиваются правильно.

Эти тесты будут проверять функциональность, которая не связана напрямую с CRUD-операциями и методом `set_level`.

Адекватная авторизация (на данный момент после регистрации перебрасывает на несуществующую страницу, но на основной функционал не влияет).