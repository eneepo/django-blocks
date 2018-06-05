import inspect
import importlib

from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from polymorphic.admin import (PolymorphicParentModelAdmin, PolymorphicChildModelAdmin,
                               PolymorphicChildModelFilter)

from . import actions
from . import models


class BlockAdminMixin(admin.ModelAdmin):
    base_model = models.Block
    date_hierarchy = 'publish_date'
    list_display = ('title', 'section', 'status',
                    'publish_date', 'expiry_date', )
    search_fields = ('title', )
    list_filter = ('section', 'status', )
    actions = (actions.mark_as_published, actions.mark_as_unpublished, )

    def get_fieldsets(self, request, obj=None):
        """
        Different fieldset for the admin form
        """
        fieldsets = [
            (None, {'fields': [
                ('title', 'show_title'), 'section', 'wrapper_css_class',
            ]}),
        ]

        if self.block_fieldsets:
            fieldsets += self.block_fieldsets

        fieldsets += [
            (_('Publication'), {
                'fields': [
                    'status',
                    ('publish_date', 'expiry_date',),
                ]}
             ),
        ]

        self.fieldsets = fieldsets
        return super(BlockAdminMixin, self).get_fieldsets(request, obj)


class BlockAdminBase(PolymorphicChildModelAdmin, BlockAdminMixin):
    pass


@admin.register(models.Block)
class BlockAdmin(PolymorphicParentModelAdmin, BlockAdminMixin):
    base_model = models.Block
    list_filter = (PolymorphicChildModelFilter, )

    def get_child_models(self):
        child_models = []
        blocks_apps = getattr(settings, "BLOCKS_APPS", None)
        for app_name in blocks_apps:
            # Dynamically loading inherited models of blocks
            # We can't use get_model of apps because of model inheritance
            module = importlib.import_module('{}.models'.format(app_name))
            app_models = inspect.getmembers(module, inspect.isclass)
            for name, model in app_models:
                if name != 'Block' and issubclass(model, models.Block):
                    child_models.append(model)
        return child_models
