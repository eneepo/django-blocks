Django Blocks
=============

Blocks is a Django app to render partial blocks of code in django
template. Blocks create a platform for others block apps to be built
upon. For example your footer is a custom HTML Block or your home page
slideshow is Carousel block. Blocks are similar to Plugins in
Django-CMS, Widgets in WordPress or Modules in Joomla!.

--------------

Overview
--------

Blocks is a flexible app to create custom blocks(sections) in your
django website. Some reasons you might want to use Blocks:

-  You don’t want to hard code every piece/section of information into
   your template.
-  And you want to dynamically change your header, footer or slide show.
-  You don’t want to use a django based CMS with tons of dependency.
-  You have migrated from WordPress or other CMS and missed how easy it
   was to add a Widget.

Requirements
------------

-  Python (3.4, 3.5, 3.6) \*
-  Django (1.11, 2.0) \*
-  `django-polymorphic`_
-  `sorl-thumbnail`_ \*\*

| *\* Not checked with other versions.*
| *\*\* It’s not mandatory. You can use whatever you want to generate
  thumbnails but you should override the templates.*


.. _django-polymorphic: https://github.com/django-polymorphic/django-polymorphic
.. _sorl-thumbnail: https://github.com/jazzband/sorl-thumbnail
.. |Django blocks: add Block| image:: https://raw.githubusercontent.com/eneepo/django-blocks/master/docs/img/screenshots/django-admin--add-block.jpg
.. |Django blocks: add Carousel block| image:: https://raw.githubusercontent.com/eneepo/django-blocks/master/docs/img/screenshots/django-admin--add-carousel-block.jpg
.. |Django blocks: add HTML block| image:: https://raw.githubusercontent.com/eneepo/django-blocks/master/docs/img/screenshots/django-admin--add-html-block.jpg