######################
pyApp - Elastic Search
######################

*Let us handle the boring stuff!*

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: http://github.com/ambv/black
   :alt: Once you go Black...

.. image:: https://github.com/pyapp-org/pyapp.elasticsearch/workflows/Python%20package/badge.svg
   :alt: Tests

.. image:: https://api.codeclimate.com/v1/badges/e25e476cd1cd598e89f4/maintainability
   :target: https://codeclimate.com/github/pyapp-org/pyapp.elasticsearch/maintainability
   :alt: Maintainability

.. image:: https://api.codeclimate.com/v1/badges/e25e476cd1cd598e89f4/test_coverage
   :target: https://codeclimate.com/github/pyapp-org/pyapp.elasticsearch/test_coverage
   :alt: Test Coverage

This extension provides a Elasticsearch client object configured via pyApp settings.


Installation
============

Install with *pip*::

    pip install pyApp-elasticsearch-py


**For AsyncIO support either**::

    pip install pyApp-elasticsearch-py[async]

    # - OR -

    pip install pyApp-elasticsearch-py aiohttp


Add the `ELASTICSEARCH` block into your runtime settings file::

    ELASTICSEARCH = {
        "default": {
            "host": "localhost",
        }
    }


.. note::

    In addition to the *host* any argument that can be provided to
    `elasticsearch.Elasticsearch` or `elasticsearch.AsyncElasticsearch` can be
    provided.


Usage
=====

The following example creates an Elasticsearch client instance::

    from pyapp_ext.elasticsearch import get_client

    es = get_client()


Or an async Elasticsearch client instance::

    from pyapp_ext.elasticsearch import get_async_client

    es = get_async_client()


API
===
