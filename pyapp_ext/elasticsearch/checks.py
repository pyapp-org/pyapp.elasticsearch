"""
Elasticsearch Checks
~~~~~~~~~~~~~~~~~~~~

"""
from pyapp.checks.registry import register
from ._factory import factory

register(factory)
