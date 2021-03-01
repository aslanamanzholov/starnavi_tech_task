from rest_framework.routers import DefaultRouter

from .views import PostViewSet, PostFeedbackViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('posts_feedback', PostFeedbackViewSet, basename='posts_feedback')

urlpatterns = []
urlpatterns += router.urls
