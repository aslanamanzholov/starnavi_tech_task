from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import UserViewSet, UserCreateViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('sign_up', UserCreateViewSet, basename='users_create')

urlpatterns = [
    path(route='api-auth/', view=include('rest_framework.urls')),
    path(route='token/', view=TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(route='refresh_token/', view=TokenRefreshView.as_view(), name='token_refresh'),
    path(route='token/verify/', view=TokenVerifyView.as_view(), name='token_verify'),
]
urlpatterns += router.urls
