from django.db import models
from django.db.models import Q
from django.utils import timezone

from . import constants


class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(
            (Q(expiry_date__gte=timezone.now()) | Q(expiry_date=None)) &
            (Q(publish_date__lte=timezone.now()) | Q(publish_date=None)) &
            Q(status=constants.STATUS_PUBLISHED)
        )
