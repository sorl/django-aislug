#coding=utf-8
from django.test import TestCase
from .models import *


class SimpleTest(TestCase):
    def test_incr(self):
        i1 = Item.objects.create(title='xxx')
        i2 = Item.objects.create(title='xxx')
        self.assertEqual(i1.title, i2.title)
        self.assertEqual(i1.slug, 'xxx')
        self.assertEqual(i2.slug, 'xxx-1')

    def test_update(self):
        item = ItemUpdateFalse.objects.create(title='xxx')
        item.title = 'yyy'
        item.save()
        self.assertEqual(item.slug, 'xxx')

    def test_slugify(self):
        item = ItemSlugify.objects.create(title=u'ÅÄÖ')
        self.assertEqual(item.slug, u'ÅÄÖ')

    def test_invalidlist(self):
        item = ItemInvalidList.objects.create(title='invalid')
        self.assertEqual(item.slug, 'invalid-1')

    def test_invalidcallback(self):
        item = ItemInvalidCallback.objects.create(title='invalid')
        self.assertEqual(item.slug, 'invalid-1')

    def test_populatefrompropery(self):
        item = ItemPopulateFromProperty.objects.create(name='yyy')
        self.assertEqual(item.slug, 'yyy')

    def test_populatefrommethod(self):
        item = ItemPopulateFromMethod.objects.create(name='yyy')
        self.assertEqual(item.slug, 'yyy')

    def test_uniquefor(self):
        i1 = ItemUniqueFor.objects.create(title='xxx', category='yyy')
        i2 = ItemUniqueFor.objects.create(title='xxx', category='zzz')
        self.assertEqual(i1.slug, i2.slug)

