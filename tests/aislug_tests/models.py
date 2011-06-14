from aislug import AISlugField
from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = AISlugField()

class ItemUpdateFalse(models.Model):
    title = models.CharField(max_length=100)
    slug = AISlugField(update=False)

class ItemSlugify(models.Model):
    title = models.CharField(max_length=100)
    slug = AISlugField(slugify=lambda x: x)

class ItemInvalidList(models.Model):
    title = models.CharField(max_length=100)
    slug = AISlugField(invalid=['invalid'])

class ItemInvalidCallback(models.Model):
    title = models.CharField(max_length=100)
    slug = AISlugField(invalid=lambda: ['invalid'])

class ItemPopulateFromProperty(models.Model):
    name = models.CharField(max_length=100)
    slug = AISlugField(populate_from='name')

class ItemPopulateFromMethod(models.Model):
    name = models.CharField(max_length=100)
    slug = AISlugField(populate_from='meth')

    def meth(self):
        return self.name

class ItemUniqueFor(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    slug = AISlugField(unique_for=['category'])

