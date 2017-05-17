from django.template import Template, Context, TemplateSyntaxError
from django.test import SimpleTestCase
from django.test.utils import override_settings


def _render(template, context={}):
    context = Context(context)
    output = Template('{% load testhook %}' + template).render(context)
    return output


class TesthookTagTests(SimpleTestCase):

    @override_settings(TESTHOOK_ENABLED=False)
    def test_testhook_disabled(self):
        self.assertEqual(_render('{% testhook "example" %}'), '')

    def test_testhook_name_only(self):
        self.assertEqual(
            _render('{% testhook "example" %}'), ' data-testhook-id="example"'
        )
        self.assertEqual(
            _render('{% testhook "example-with-dash" %}'),
            ' data-testhook-id="example-with-dash"'
        )

        self.assertEqual(
            _render('{% testhook "Just Do It" %}'),
            ' data-testhook-id="just-do-it"'
        )
        self.assertEqual(
            _render('{% testhook "Just_Do_It" %}'),
            ' data-testhook-id="just_do_it"'
        )

    def test_testhook_no_name(self):
        self.assertRaises(TemplateSyntaxError, _render, '{% testhook %}')

    def test_testhook_invalid_name_property(self):
        context = {"obj": {"example": "object", "not": "allowed"}}
        self.assertRaises(
            TemplateSyntaxError, _render, '{% testhook obj %}', context
        )

    def test_testhook_additional_arguments(self):
        self.assertEqual(
            _render('{% testhook "prepend" "addon" %}'),
            ' data-testhook-id="prepend-addon"'
        )

        self.assertEqual(
            _render('{% testhook "prepend" "Add On" %}'),
            ' data-testhook-id="prepend-add-on"'
        )

        context = {"product": {"id": 1, "slug": "unique-slug"}}
        self.assertEqual(
            _render(
                '{% testhook "prepend" product.id product.slug %}',
                context
            ),
            ' data-testhook-id="prepend-1-unique-slug"'
        )
