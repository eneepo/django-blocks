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
        ('Carousel settings', {'fields': [
            ('has_controls', 'has_indicators', 'has_captions'),
            'interval', 'keyboard', 'pause', 'ride', 'wrap',
        ]}),
        ('Caption settings', {'fields': [
            'crop_size', 'image_css_class', 'caption_css_class',
        ]}),
    ]

    # class Media:
    #     js = (
    #         '//cdn.ckeditor.com/4.9.2/standard/ckeditor.js',
    #         'blocks/js/html.js',
    #     )
    #     css = {
    #         'all': ()
    #     }
