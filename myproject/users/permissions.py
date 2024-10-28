from rest_framework.permissions import BasePermission, SAFE_METHODS

class UserPermission(BasePermission):
    """
    Кастомное разрешение для проверки прав пользователей на редактирование и удаление.
    - Только пользователи в группе "admin" могут удалять других пользователей.
    - Пользователи в группе "editor" могут только редактировать данные.
    """

    def has_permission(self, request, view):
        # Ограничим доступ для создания и удаления, доступен только для администраторов
        if view.action in ['create', 'destroy']:
            return request.user.groups.filter(name='admin').exists()

        # Разрешим чтение для всех авторизованных пользователей
        if view.action in ['list', 'retrieve']:
            return request.user.is_authenticated

        # Разрешим редактирование только для пользователей группы "editor" или "admin"
        if view.action in ['update', 'partial_update']:
            return request.user.groups.filter(name__in=['admin', 'editor']).exists()

        return False
