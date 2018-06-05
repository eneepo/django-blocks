from django.contrib import admin

from blocks.admin import BlockAdminBase
from .models import Alert


@admin.register(Alert)
class HtmlAdmin(BlockAdminBase):
    block_fieldsets = [
        ('Alert options', {'fields': [
            'style', 'has_dismiss_button', 'content',
        ]}),
    ]

    class Media:
        js = (
            '//cdn.ckeditor.com/4.9.2/standard/ckeditor.js',
            'blocks/js/alerts-admin.js',
        )
