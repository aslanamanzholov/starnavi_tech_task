import django_filters

from .models import PostFeedback


class PostFeedbackFilter(django_filters.rest_framework.FilterSet):
    date = django_filters.DateFromToRangeFilter(field_name="date")

    class Meta:
        model = PostFeedback
        fields = ['date', 'post', 'user']
