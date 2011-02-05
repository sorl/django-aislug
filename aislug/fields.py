from django.db import models
from aislug.helpers import slugify


class AISlugField(models.SlugField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 110)
        kwargs.setdefault('unique', True)
        kwargs.setdefault('editable', False)
        self.update = kwargs.pop('update', True)
        self.populate_from = kwargs.pop('populate_from', 'title')
        self.slugify = kwargs.pop('slugify', slugify)
        self.invalid = kwargs.pop('invalid', [])
        self.queryset = kwargs.pop('queryset', None)
        super(AISlugField, self).__init__(*args, **kwargs)

    def pre_save(self, obj, add):
        if add or self.update:
            value = getattr(obj, self.populate_from)
            if callable(value):
                value = value()
        else:
            value = self.value_from_object(obj)
        slug = self.slugify(value)
        if self.queryset is None:
            queryset = obj.__class__._default_manager
        else:
            queryset = self.queryset
        queryset = queryset.filter(**{'%s__startswith' % self.attname: slug})
        if not add:
            queryset = queryset.exclude(pk=obj.pk)
        if callable(self.invalid):
            invalid = self.invalid()
        else:
            invalid = self.invalid[:]
        invalid.extend(list(queryset.values_list(self.attname, flat=True)))
        _slug = slug
        counter = 1
        while True:
            if _slug not in invalid:
                break
            _slug = '%s-%s' % (slug, counter)
            counter += 1
        slug = _slug
        setattr(obj, self.attname, slug)
        return slug

    def south_field_triple(self):
        from south.modelsinspector import introspector
        args, kwargs = introspector(self)
        return ('django.db.models.fields.SlugField', args, kwargs)

