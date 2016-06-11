from django.template import Library, TemplateSyntaxError
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.text import slugify

register = Library()


@register.simple_tag
def testhook(name, *args):
    if not getattr(settings, 'TESTHOOK_ENABLED', True):
        return u''

    if not name:
        raise TemplateSyntaxError(
            'Invalid testhook argument for name, expected non empty string'
        )

    if not isinstance(name, basestring):
        raise TemplateSyntaxError(
            'Invalid testhook argument for name, expected string'
        )

    # slugify the name by default
    name = slugify(name)

    if args:
        name = '{}-{}'.format(name, '-'.join(filter(None, args)))

    return mark_safe(u'data-testhook-id="{0}"'.format(name))
