from django import template

from blocks.models import Block

register = template.Library()


@register.inclusion_tag('blocks/block.html')
def render_block(section):
    items = Block.objects.filter(section=section)

    return {
        'items': items,
    }
