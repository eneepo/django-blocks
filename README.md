# Django Blocks
Blocks is a Django app to render partial blocks of code in django template.
Blocks create a platform for others block apps to be built upon. For example
your footer is a custom HTML Block or your home page slideshow is Carousel block.
Blocks are similar to Plugins in Django-CMS, Widgets in WordPress or Modules in Joomla!.

---

## Overview

Blocks is a flexible app to create custom blocks(sections) in your django website.
Some reasons you might want to use Blocks:

* You don't want to hard code every piece/section of information into your template.
* And you want to dynamically change your header, footer or slide show.
* You don't want to use a django based CMS with tons of dependency.
* You have migrated from WordPress or other CMS and missed how easy it was to add a Widget.

## Requirements
* Python (3.4, 3.5, 3.6) *
* Django (1.11, 2.0) *
* [django-polymorphic][polymorphic-url]
* [sorl-thumbnail][sorl-thumbnail-url] **

_\* Not checked with other versions._  
_\*\* It's not mandatory. You can use whatever you want to generate thumbnails but you should 
override the templates._

## Installation
Install using `pip`...

    pip install django-blocks

Add `'blocks'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = (
        ...
        'blocks',
    )

Add sections that you want to `BLOCKS_SECTIONS` setting.

    BLOCKS_SECTIONS = (
        ('sidebar', 'header'),
        ('sidebar', 'Sidebar'),
        ('footer', 'Footer'),
    )

Add block apps that you want to use to `BLOCKS_APPS` setting. 
There's no need to add these apps to `INSTALLED_APPS`. 

    BLOCKS_APPS = (
        'blocks.html',
        'blocks.carousels',
    )

In your template load `blocks` and use `{% render_block 'your_section' %}` to
render the blocks in the sections you defined in the `BLOCKS_SECTIONS`.

    {% load blocks %}
    {% render_block 'sidebar' %}

Use admin to create a custom HTML block or a Carousel block.

## Admin app settings
### General settings
To be written soon

### HTML Block
To be written soon

### Carousel Block
To be written soon

## Create a Custom SubBlock
To be written soon

## Todo
* Add caching
* Create documentation
* Tests

[polymorphic-url]: https://github.com/django-polymorphic/django-polymorphic
[sorl-thumbnail-url]: https://github.com/jazzband/sorl-thumbnail