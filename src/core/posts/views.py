from django.contrib.auth import get_user_model
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .filters import PostFeedbackFilter
from .models import Post, PostFeedback
from .serializers import PostSerializer, PostFeedbackSerializer

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        created_by = self.request.user
        serializer.save(created_by=created_by)

    @action(methods=['GET'], detail=True)
    def post_feedback(self, request, pk):
        instance = self.get_object()
        post_feedback = PostFeedback.objects.all()
        if post_feedback.filter(user=self.request.user, post=instance).exists():
            liked = False
            # if PostFeedback have records with user and post delete such unlike.
            post_feedback.filter(user=self.request.user, post=instance).delete()
        else:
            liked = True
            # if PostFeedback have not records with user and post instance.
            PostFeedback.objects.create(user=self.request.user, post=instance)
        context = {
            'post': PostSerializer(instance).data,
            'liked': liked,
            'total_likes': post_feedback.filter(post=instance).count(),
        }
        return Response(context, status=status.HTTP_200_OK)


class PostFeedbackViewSet(viewsets.ModelViewSet):
    queryset = PostFeedback.objects.all()
    serializer_class = PostFeedbackSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFeedbackFilter

    @action(methods=['GET'], detail=False)
    def analitics(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        # filter queryset by day.
        posts_feedback = queryset.extra({"day": "date_trunc('day', date)"}).values(
            "day").order_by().annotate(count=Count("id"))
        return Response(posts_feedback, status=status.HTTP_200_OK)
