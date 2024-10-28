from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, user_list

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', user_list, name='user_list'),
]
