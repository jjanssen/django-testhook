# django-testhook (WIP)
A Django template tag to enable testhook attributes on HTML elements.

.. image:: https://travis-ci.org/jjanssen/django-testhook.svg?branch=master
    :target: http://travis-ci.org/jjanssen/django-testhook
.. image:: https://img.shields.io/pypi/v/django-testhook.svg
    :target: https://pypi.python.org/pypi/django-testhook/
.. image:: https://img.shields.io/pypi/dm/django-testhook.svg
    :target: https://pypi.python.org/pypi/django-testhook/
.. image:: https://img.shields.io/badge/wheel-yes-green.svg
    :target: https://pypi.python.org/pypi/django-testhook/
.. image:: https://img.shields.io/pypi/l/django-testhook.svg
    :target: https://pypi.python.org/pypi/django-testhook/
.. image:: https://img.shields.io/pypi/pyversions/Django.svg
    :target: https://pypi.python.org/pypi/django-testhook/
.. image:: https://coveralls.io/repos/jjanssen/django-testhook/badge.svg?branch=master
    :target: https://coveralls.io/github/jjanssen/django-testhook?branch=master

## About django-testhook

The django-testhook provides a template tag to generate `data-testhook-id` for HTML templates.

This can be useful for automated testing (for eg: [Webdriver.IO](http://www.webdriver.io)) to maintain a fixed entry point, rather than having a automated test that breaks by just renaming a CSS class or an element which can require you to re-evaluate an XPath-selector.

## Requirements

Django 1.8.x or greater, Python 2.7 or greater.

## Installation

Install django-testhook with pip:

    $ pip install django-testhook

## Configuration

### Configuring django-testhook

Add the following to your settings file:

```python
INSTALLED_APPS += (
    'testhook',
)
```

### Available settings

By default the rendering of testhook data attributes is enabled.
If you are in the scenario you want to disable it for a certain environment just configure it to `False`.

```python
TESTHOOK_ENABLED = False
```

## Usage

### Basic usage

Within your HTML template you must load the testhook tag in order to use it.
The testhook tag only requires a single argument in order to return a result.

```HTML
{% load testhook %}

<div class="my-elem" {% testhook "test-elem" %}>
    I want to test this
</div>
```

This will output to the following:

```HTML
<div class="my-elem" data-testhook-id="test-elem">
    I want to test this
</div>
```

### Object Usage

For dynamic elements there is also the option to pass arguments.
For eg: given I have a product in a shopping basket with a primary key and a slug I could use it like this:

```HTML
<div class="item" {% testhook "basket" product.id product.slug %}>
    {{ product.title }}
</div>
```

It will output to:
```HTML
<div class="item" data-testhook-id="basket-1-product-slug">
    A product title
</div>
```
