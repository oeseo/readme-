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

