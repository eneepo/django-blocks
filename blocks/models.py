from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from polymorphic.models import PolymorphicModel

from .managers import PublishManager
from . import constants


class PublishMixin(models.Model):
    status = models.IntegerField(
        _("Status"),
        choices=constants.STATUS_CHOICES,
        default=constants.STATUS_UNPUBLISHED,
        db_index=True,
        help_text=_(
            "Only admins can see unpublished items."
        )
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True,
        blank=True,
    )
    publish_date = models.DateTimeField(
        _("Published from"),
        help_text=_("With Published chosen, won't be shown until this time"),
        blank=True,
        null=True,
        db_index=True
    )
    expiry_date = models.DateTimeField(
        _("Expires on"),
        help_text=_("With Published chosen, won't be shown after this time"),
        blank=True,
        null=True
    )

    published = PublishManager()

    class Meta:
        abstract = True
        ordering = ['-publish_date']

    def save(self, *args, **kwargs):
        if not self.publish_date and not self.created:
            self.publish_date = timezone.now()
        elif not self.publish_date:
            self.publish_date = self.created
        super(PublishMixin, self).save(*args, **kwargs)

    def get_publish_date(self):
        return self.publish_date if self.publish_date else self.created

    def get_previous(self):
        item = self._meta.model.published.order_by('-publish_date').filter(
            publish_date__lt=self.publish_date
        )
        return item[0] if item else None

    def get_next(self):
        item = self._meta.model.published.order_by('-publish_date').filter(
            publish_date__gt=self.publish_date
        )
        return item[0] if item else None

    @property
    def is_published(self):
        if self.status == constants.STATUS_PUBLISHED:
            return True
        else:
            return

    @property
    def is_unpublished(self):
        if self.status == constants.STATUS_UNPUBLISHED:
            return True
        else:
            return


class Block(PolymorphicModel, PublishMixin):
    title = models.CharField(_('Title'), max_length=255, db_index=True)
    show_title = models.BooleanField(_('Show title'), default=False)

    BLOCKS_SECTIONS = getattr(settings, "BLOCKS_SECTIONS", None)
    section = models.CharField(_('Section'), max_length=255, choices=BLOCKS_SECTIONS,
                               blank=True, null=True,)

    wrapper_css_class = models.CharField(
        _('Wrapper css class'), max_length=255, db_index=True, blank=True, null=True,
        help_text=_(
            ''' You can use the <b>invisible</b> class to hide the element and later remove 
            the invisible class with some conditions using js. 
            '''
        )
    )

    class Meta:
        app_label = 'blocks'

    def get_template(self):
        return 'blocks/block_{}.html'.format(self.__class__.__name__.lower())

    @property
    def template(self):
        return self.get_template()
