from django.contrib import admin

from polymorphic.admin import PolymorphicChildModelAdmin

from blocks.admin import BlockAdminBase
from . import models


class SlideStackedInline(admin.StackedInline):
    model = models.Slide
    extra = 0


@admin.register(models.Carousel)
class HtmlAdmin(PolymorphicChildModelAdmin, BlockAdminBase):
    inlines = (SlideStackedInline,)
    block_fieldsets = [
        ('Carousel options', {'fields': [
            ('has_controls', 'has_indicators', 'has_captions'),
            'interval', 'keyboard', 'pause', 'ride', 'wrap',
        ]}),
        ('Caption options', {'fields': [
            'crop_size', 'image_css_class', 'caption_css_class',
        ]}),
    ]

