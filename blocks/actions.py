''' Mark as active or inactive actions
'''
from django.contrib import messages

from . import constants


def mark_as_published(modeladmin, request, queryset):
    ''' Makes selected objects published
    '''
    rows_updated = queryset.update(status=constants.STATUS_PUBLISHED)
    if rows_updated == 1:
        message = '1 item'
    else:
        message = '{} items were'.format(rows_updated)
    messages.success(
        request,
        '{} successfully marked as published.'.format(message)
    )


mark_as_published.short_description = 'Mark items as published'


def mark_as_unpublished(modeladmin, request, queryset):
    ''' Makes selected objects unpublished
    '''
    rows_updated = queryset.update(status=constants.STATUS_UNPUBLISHED)
    if rows_updated == 1:
        message = '1 item'
    else:
        message = '{} items were'.format(rows_updated)
    messages.success(
        request,
        '{} successfully marked as unpublished.'.format(message)
    )


mark_as_unpublished.short_description = 'Mark items as unpublished'
