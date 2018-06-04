from django.db import models
from django.utils.translation import ugettext_lazy as _

from blocks.models import Block


class Carousel(Block):
    has_controls = models.BooleanField(
        _("With controls"),
        default=True,
        help_text=_("If true, adds the previous and next controls")
    )
    has_indicators = models.BooleanField(
        _("With indicators"),
        default=True,
        help_text=_("If true, adds indicators to the carousel")
    )
    has_captions = models.BooleanField(
        _("With captions"),
        default=True,
        help_text=_("If true, adds captions to the carousel")
    )

    interval = models.IntegerField(
        default=5000,
        help_text=_("The amount of time to delay between automatically cycling an item. "
                    "If false, carousel will not automatically cycle.")
    )
    keyboard = models.BooleanField(
        default=True,
        help_text=_("Whether the carousel should react to keyboard events.")
    )
    pause = models.BooleanField(
        default=True,
        help_text=_(
            """If set to "True", pauses the cycling of the carousel on mouseenter 
            and resumes the cycling of the carousel on mouseleave.
            If set to "False", hovering over the carousel won't pause it.""")
    )
    ride = models.BooleanField(
        default=False,
        help_text=_("Autoplays the carousel after the user manually cycles the first item. "
                    'If "True", autoplays the carousel on load.')
    )
    wrap = models.BooleanField(
        default=True,
        help_text=_("Whether the carousel should cycle continuously or have hard stops.")
    )

    crop_size = models.CharField(_('Crop size'), max_length=255, blank=True, null=True)
    image_css_class = models.CharField(_('Image css class'), max_length=255, db_index=True,
                                       blank=True, null=True)
    caption_css_class = models.CharField(_('Caption css class'), max_length=255, db_index=True,
                                         blank=True, null=True)

    class Meta:
        app_label = 'blocks'
        verbose_name = 'Carousel Block'
        verbose_name_plural = 'Carousel Blocks'


class Slide(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE, related_name='slides')

    title = models.CharField(_('Title'), max_length=255, blank=True, null=True)
    caption = models.TextField(_('Caption'), blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to="blocks/carousels")

    class Meta:
        app_label = 'blocks'
        verbose_name = 'Carousel Block Slide'
        verbose_name_plural = 'Carousel Block Slides'
