# 1. Установка и настройка Django проекта


### Устанавливаем Django и Django REST framework
pip install django djangorestframework djangorestframework-simplejwt

### Создаем новый Django проект
django-admin startproject myproject
cd myproject

### Создаем приложение для пользователей
python manage.py startapp users

# 2. Настроить проекта
### В файле myproject/settings.py добавьте rest_framework, rest_framework.authtoken, и приложение users в INSTALLED_APPS

# 3. Создать кастомной модели пользователя
### В файле users/models.py создайте кастомную модель пользователя и настройте модель пользователя в myproject/settings.py

# 4. Создать сериализаторов
### В файле users/serializers.py создайте два сериализаторы для пользователей

# 5. Создать API представлений
### В файле users/views.py создайте API для работы с пользователями

# 6. Настроть маршрутов
### В файле users/urls.py настройте маршруты для API и в myproject/urls.py подключите users.urls

# 7. Аутентификация по JWT-токену
### Добавь JWT-маршруты в myproject/urls.py

# 8. Создать фронтенда с таблицей пользователей
### В директории users/templates/users создать файл index.html, содержащий таблицу для отображения пользователей

# 9. Настройка прав доступа
### В users/views.py добавить права доступа для редактирования и удаления

Проект представляет собой Django-приложение для управления пользователями с использованием Django REST Framework и аутентификации по JWT.

## Основные функции
- Кастомная модель пользователя с полями ФИО, должность, статус увольнения и дата увольнения.
- API для получения списка пользователей с фильтрацией по статусу увольнения.
- Аутентификация по JWT-токену.
- Простой фронтенд для отображения пользователей в таблице.

## Установка
1. Клонируйте репозиторий.
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
3. Запустите сервер:
   ```bash
   python manage.py runserver
