from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractCreatedByTrackable(models.Model):
    created_by = models.ForeignKey(
        'users.User',
        verbose_name=_("created by"),
        related_name="%(app_label)s_%(class)s_created_by",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True
