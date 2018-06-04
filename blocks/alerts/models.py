from django.db import models
from django.utils.translation import ugettext_lazy as _

from blocks.models import Block


class Alert(Block):
    STYLE_PRIMARY = 'primary'
    STYLE_SECONDARY = 'secondary'
    STYLE_SUCCESS = 'success'
    STYLE_DANGER = 'danger'
    STYLE_WARNING = 'warning'
    STYLE_INFO = 'info'
    STYLE_LIGHT = 'light'
    STYLE_DARK = 'dark'

    STYLE_CHOICES = (
        (STYLE_PRIMARY, "Primary"),
        (STYLE_SECONDARY, "Secondary"),
        (STYLE_SUCCESS, "Success"),
        (STYLE_DANGER, "Danger"),
        (STYLE_WARNING, "Warning"),
        (STYLE_INFO, "Info"),
        (STYLE_LIGHT, "Light"),
        (STYLE_DARK, "Dark"),
    )

    style = models.CharField(
        _("Style"),
        choices=STYLE_CHOICES,
        max_length=50,
        help_text=_(
            ''' For proper styling, use one of the eight required contextual classes, 
            <a href="https://getbootstrap.com/docs/4.1/components/alerts/#examples">
            view this examples to get the idea</a>.'''
        )
    )

    has_dismiss_button = models.BooleanField(
        _("Has dismiss button"),
        default=True,
        help_text=_(
            ''' Remember to use dismiss alerts only once, in other words
            don't edit the content to reuse the block again. Once published, create another one.
            '''
        )
    )

    content = models.TextField(
        _('Content'), null=True, blank=True,
        help_text=_(
            ''' Use the <b>.alert-link</b> utility class to quickly provide matching colored links within any alert, 
            <a href="https://getbootstrap.com/docs/4.1/components/alerts/#link-color">view this examples 
            to get the idea</a>. Also you can use <b>.alert-heading</b> for force elements to inherit text color.
            '''
        )
    )

    class Meta:
        app_label = 'blocks'
        verbose_name = 'Alert Block'
        verbose_name_plural = 'Alert Blocks'

