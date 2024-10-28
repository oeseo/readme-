from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['is_dismissed']

    # Дополнительный метод для фильтрации пользователей по статусу
    @action(detail=False, methods=['get'])
    def filter_by_dismissed(self, request):
        is_dismissed = request.query_params.get('is_dismissed', 'false').lower() == 'true'
        users = CustomUser.objects.filter(is_dismissed=is_dismissed)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            permission_classes = [IsAuthenticated]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

# Create your views here.
