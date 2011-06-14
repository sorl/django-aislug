from aislug import AISlugField
from stringfield import StringField
from django.core.exceptions import ValidationError
from django.test import TestCase


class ValidationTest(TestCase):
    def test_aislug_raises_error_on_empty_string(self):
        f = AISlugField()
        self.assertEqual('', f.clean('', None))

    def test_aislug_cleans_empty_string_when_blank_true(self):
        f = AISlugField(blank=False, editable=True)
        self.assertRaises(ValidationError, f.clean, "", None)

    def test_aislug_with_choices_cleans_valid_choice(self):
        f = AISlugField(max_length=1, choices=[('a','A'), ('b','B')])
        self.assertEqual('a', f.clean('a', None))

    def test_aislug_with_choices_raises_error_on_invalid_choice(self):
        f = AISlugField(choices=[('a','A'), ('b','B')], editable=True)
        self.assertRaises(ValidationError, f.clean, "not a", None)

    def test_aislug_raises_error_on_empty_input(self):
        f = AISlugField(null=False, editable=True)
        self.assertRaises(ValidationError, f.clean, None, None)

