import os

from django.apps import AppConfig
from django.conf import settings


class BlocksConfig(AppConfig):
    name = 'blocks'

    def ready(self):
        for block_name in getattr(settings, "BLOCKS_APPS", None):
            if block_name not in settings.INSTALLED_APPS:
                settings.INSTALLED_APPS += (block_name, )
