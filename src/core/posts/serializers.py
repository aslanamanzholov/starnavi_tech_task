from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post, PostFeedback
from ..helpers.constants import FEEDBACK_CHOICES
from ..users.serializers import UserListSerializer

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    liked_users = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('created_by',)

    def get_likes(self, obj):
        return obj.post_feedback.count()

    def get_liked_users(self, obj):
        arr = []
        pf = PostFeedback.objects.filter(post_id=obj.id)
        for i in pf:
            arr.append(i.user)
        return UserListSerializer(arr, many=True).data


class PostFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFeedback
        fields = '__all__'


class PostFeedbackAcceptSerializer(serializers.Serializer):
    type_of_feedback = serializers.ChoiceField(choices=FEEDBACK_CHOICES, required=True)
