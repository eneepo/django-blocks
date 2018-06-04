from django.utils.translation import ugettext_lazy as _


STATUS_UNPUBLISHED = 1
STATUS_PUBLISHED = 2

STATUS_CHOICES = (
    (STATUS_UNPUBLISHED, _("Unpublished")),
    (STATUS_PUBLISHED, _("Published")),
)