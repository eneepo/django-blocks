Quickstart
==========

Installation
------------

Install using ``pip``

::

   pip install django-blocks

Settings Configuration
----------------------

Add ``'blocks'`` to your ``INSTALLED_APPS`` setting.

::

   INSTALLED_APPS = (
       ...
       'blocks',
   )

Add following sections to your django settings.

::

   # Add sub-blocks that you want to use
   BLOCKS_APPS = (
       'blocks.alerts',
       'blocks.carousels',
       'blocks.html',
   )

   # Add tuples of sections that you want to render sub-blocks into
   BLOCKS_SECTIONS = (
       ('header', 'Header'),
       ('sidebar', 'Sidebar'),
       ('footer', 'Footer'),
   )


Template Rendering
------------------

In your template load blocks and use
``{% render_block 'your_section' %}`` to render the blocks in the
sections you defined in the ``BLOCKS_SECTIONS``.

::

   {% load blocks %}

   {% render_block 'sidebar' %}

Use admin to create :ref:`alert-block`, :ref:`carousel-block`, :ref:`html-block` or
create your own :ref:`custom-block`.
