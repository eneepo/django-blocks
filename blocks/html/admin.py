from django.contrib import admin

from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicChildModelFilter

from blocks.admin import BlockAdminBase
from .models import Html


@admin.register(Html)
class HtmlAdmin(PolymorphicChildModelAdmin, BlockAdminBase):
    block_fieldsets = [
        ('Html Code', {'fields': [
            'code',
        ]}),
    ]

    class Media:
        js = (
            '//cdn.ckeditor.com/4.9.2/standard/ckeditor.js',
            'blocks/js/html.js',
        )
        css = {
            'all': ()
        }