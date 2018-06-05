from django.conf import settings

blocks_apps = getattr(settings, "BLOCKS_APPS", None)

if blocks_apps:
    for block_name in blocks_apps:
        if block_name not in settings.INSTALLED_APPS:
            settings.INSTALLED_APPS += (block_name, )
