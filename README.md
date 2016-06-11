# django-testhook (WIP)
A Django template tag to enable testhook attributes on HTML elements.

## About django-testhook

The django-testhook provides a template tag to generate `data-testhook-id` for HTML templates.

This can be useful for automated testing (for eg: [Webdriver.IO](http://www.webdriver.io)) to maintain a fixed entry point, rather than having a automated test that breaks by just renaming a CSS class or an element which can require you to re-evaluate an XPath-selector.

## Requirements

Django 1.8.x or greater, Python 2.7 or greater.
