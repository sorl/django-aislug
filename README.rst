django-aislug
=============

A slug field that automatically calculates its value.

Options
-------
All options that are available for ``django.db.models.SlugField`` are also
available ``AISlugField``.

- ``populate_from``: Property on the model that is the base for the computed
  slug, defaults to ``'title'``

- ``slugify``: User defined slugify callback function to compute the slug from
  ``populate_from``

- ``invalid``: List or function that returns a list of invalid values

- ``queryset``: Queryset to use for making the slug unique within
  the queryset scope, default value is the default manager

- ``update``: If false the slug will not be updated  from ``populate_from`` on
  subsequent saves.

