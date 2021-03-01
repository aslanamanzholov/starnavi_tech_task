from django.contrib.auth import get_user_model
from django.db import models

from ..helpers.abstract import AbstractCreatedByTrackable

from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Post(AbstractCreatedByTrackable):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Post title'))

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return '{}'.format(self.title)


class PostFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_feedback')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_feedback')
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Post Feedback'
        verbose_name_plural = 'Posts Feedback'

    def __str__(self):
        return '{} - {}'.format(self.post, self.user.username)
