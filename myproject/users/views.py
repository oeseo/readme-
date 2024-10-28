from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Position
from .serializers import UserSerializer, PositionSerializer
from .permissions import UserPermission
from django.shortcuts import render

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['is_dismissed']
    permission_classes = [IsAuthenticated, UserPermission]

def user_list(request):
    return render(request, 'index.html')
