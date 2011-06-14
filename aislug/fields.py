from aislug.helpers import slugify
from django.db import models
from django.db.models import Q
from stringfield import StringField


class AISlugField(StringField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('db_index', True)
        kwargs.setdefault('editable', False)
        self.update = kwargs.pop('update', True)
        self.populate_from = kwargs.pop('populate_from', 'title')
        self.slugify = kwargs.pop('slugify', slugify)
        self.invalid = kwargs.pop('invalid', [])
        self.unique_for = kwargs.pop('unique_for', [])
        if not self.unique_for:
            kwargs.setdefault('unique', True)
        super(AISlugField, self).__init__(*args, **kwargs)

    def pre_save(self, obj, add):
        value = self.value_from_object(obj)
        if add or self.update:
            # only compute slug if its a new record or if we have update set
            if not self.editable or not value:
                # if editable is True the user can set the base for slug
                # themselves, however if the user passes an empty slug that
                # means we should calculate it.
                value = getattr(obj, self.populate_from)
                if callable(value):
                    value = value()
        slug = self.slugify(value)
        queryset = obj.__class__._default_manager
        # filter out the ones that we should make the slug unique for
        # Note that the slug attr cannot be part of this list.
        q = Q()
        for attr in self.unique_for:
            if attr != self.attname:
                q = q & Q(**{attr: getattr(obj, attr)})
        queryset = queryset.filter(q)
        # This will give us the invalid slugs in one query instead of checking
        # in each iteration in the below while loop.
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
        return ('stringfield.base.StringField', args, kwargs)

