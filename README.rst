
django-aislug
=============

A slug field that automatically calculates its value from another attribute or
method.

Requirements
------------
django-aislug depends on `django-stringfield <https://github.com/aino/django-stringfield>`_.

Installation
------------
Using pip to install will install django-aislug and all of its dependencies::

    pip install django-aislug

Options
-------
All options that are available for ``django.db.models.CharField`` are also
available to ``AISlugField``. There are some additional options:

* ``populate_from``: Property or method on the model that is the base for the
  computed slug.

  * Default ``'title'``

* ``slugify``: User defined slugify callback function to compute the slug from
  ``populate_from``

* ``invalid``: List or function that returns a list of invalid values

  * Default: ``[]``

* ``update``: If ``False`` the slug will not be updated from ``populate_from``
  on subsequent saves.

  * Default: ``False``

* ``unique_for``: A list of fields to make this slug unique for.

  * Default: ``[]``

