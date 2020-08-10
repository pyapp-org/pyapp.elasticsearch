ELASTICSEARCH = {
    "default": {}
}
"""
Elasticsearch server settings, see _`elasticsearch-py` docs for all available options

.. _elasticsearch-py: https://elasticsearch-py.readthedocs.io/en/master/index.html

Example settings::

    # With security and via HTTPS using RFC-1738 URL
    ELASTICSEARCH = {
        "default": {"hosts": ["https://user:secret@host1:443]},
    }
    
    # - OR -
    
    # With security and via HTTPS (long form)
    ELASTICSEARCH = {
        "default": {
            "hosts": ["host1", "host2"],
            "http_auth": ("user", "secret"),
            "scheme": "https",
            "port": 443,
        },
    }

"""
