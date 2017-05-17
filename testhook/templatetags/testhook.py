import sys
from django.template import Library, TemplateSyntaxError
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.text import slugify

if sys.version_info[0] == 3:
    basestring = str

register = Library()


@register.simple_tag
def testhook(name, *args):
    if not getattr(settings, 'TESTHOOK_ENABLED', True):
        return u''

    if not isinstance(name, basestring):
        raise TemplateSyntaxError(
            'Testhook takes at least one argument (string)'
        )

    if args:
        filtered = filter(None, args)
        concatted = '-'.join(str(x) for x in filtered)
        name = '{}-{}'.format(name, concatted)

    return mark_safe(
        u' data-testhook-id="{0}"'.format(
            slugify(name)
        )
    )
