from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, UserCreateSerializer
from ..helpers.mixins import ActionSerializerViewSetMixin


class UserViewSet(ActionSerializerViewSetMixin, viewsets.ModelViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_classes = {
        'create': UserCreateSerializer,
        ('update', 'partial_update'): UserSerializer,
        ('list', 'retrieve'): UserSerializer,
    }
    http_method_names = ['get', 'delete', 'put', 'patch']
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET'], detail=True)
    def get_user_activity(self, request, pk):
        instance = self.get_object()
        return Response({'username': instance.username, 'last_login': instance.last_login,
                         'last_activity': instance.last_activity},
                        status=status.HTTP_200_OK)


class UserCreateViewSet(ActionSerializerViewSetMixin, viewsets.ModelViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = User.objects.all()
    serializer_classes = {
        'create': UserCreateSerializer,
        ('update', 'partial_update'): UserSerializer,
        ('list', 'retrieve'): UserSerializer,
    }
    http_method_names = ['post']
    permission_classes = (AllowAny,)
