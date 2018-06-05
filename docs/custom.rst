.. _custom-block:

Custom Blocks
=============

You can start creating your own sub-block by creating a python package with
``admin.py`` and ``models.py``.

::

    example/
        __init__.py
        admin.py
        models.py

Subclass your model from :py:class:`blocks.models.Block`

.. code-block:: python

    """
    Example block model.
    """
    from django.db import models
    from blocks.models import Block


    class Example(Block):
        # Define your fields just like how you define django models
        caption = models.TextField(blank=True)

        class Meta:
            app_label = 'blocks'
            verbose_name = 'Example Block'
            verbose_name_plural = 'Example Blocks'

Subclass your admin from :py:class:`blocks.admin.BlockAdminBase`

.. code-block:: python

    """
    Example block admin.
    """
    from django.contrib import admin
    from blocks.admin import BlockAdminBase
    from .models import Example


    @admin.register(Html)
    class HtmlAdmin(BlockAdminBase):
        # Use block_fieldsets instead of fieldsets
        block_fieldsets = [
            ('Example block options', {'fields': [
                'caption',
            ]}),
        ]

        # In case your block needs custom js and css
        class Media:
            js = (
                'blocks/js/example-admin.js',
            )
            css = {
                'all': ('blocks/css/example-admin.css',)
            }

Add your example block to ``BLOCKS_APPS`` in your ``settings.py``

::

   BLOCKS_APPS = (
       ...
       'example',
   )

And finally create migration and migrate your data. Your custom sub-block is ready
to be used in admin area. Go to ``Blocks > Block > Add Block`` and select your
example sub-block in the ``Type field``.