from django.db import models
from django.utils.translation import ugettext_lazy as _

from blocks.models import Block


class Html(Block):
    code = models.TextField(_('Code'), blank=True)

    class Meta:
        app_label = 'blocks'
        verbose_name = 'HTML Block'
        verbose_name_plural = 'HTML Blocks'