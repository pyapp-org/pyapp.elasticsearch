import pytest


from pyapp_ext.elasticsearch import _factory


def test_can_get_client():
    actual = _factory.get_client()

    assert isinstance(actual, _factory.Elasticsearch)


def test_can_get_async_client():
    actual = _factory.get_async_client()

    assert isinstance(actual, _factory.AsyncElasticsearch)


def test_error_is_raised_if_asyncio_not_available(monkeypatch):
    monkeypatch.setattr(_factory, "AsyncElasticsearch", None)

    with pytest.raises(RuntimeError, match="AsyncElasticsearch is not available"):
        _factory.get_async_client()
