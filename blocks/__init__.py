from django.conf import settings

for block_name in getattr(settings, "BLOCKS_APPS", None):
    if block_name not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS += (block_name, )
