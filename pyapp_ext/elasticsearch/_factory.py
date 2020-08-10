"""
Elasticsearch Client Factory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from elasticsearch import Elasticsearch

try:
    from elasticsearch import AsyncElasticsearch
except ImportError:  # pragma: no cover
    AsyncElasticsearch = None

from pyapp.conf.helpers import NamedFactory

__all__ = (
    "factory",
    "get_client",
    "Elasticsearch",
    "async_factory",
    "get_async_client",
    "AsyncElasticsearch",
)


FACTORY_DEFAULTS = {
    "hosts": None,
}
FACTORY_OPTIONAL_KEYS = (
    # Connection options (these vary by the connection type)
    "port",
    "url_prefix",
    "timeout",
    "http_auth",
    "use_ssl",
    "verify_certs",
    "ssl_show_warn",
    "ca_certs",
    "client_cert",
    "client_key",
    "ssl_version",
    "ssl_assert_hostname",
    "ssl_assert_fingerprint",
    "maxsize",
    "headers",
    "http_compress",
    "cloud_id",
    "api_key",
    "opaque_id",
    # Transport options
    "sniff_on_start",
    "sniff_on_connection_fail",
    "sniffer_timeout",
    "default_mimetype",
    "max_retries",
    "retry_on_status",
    "retry_on_timeout",
    "send_get_body_as",
)


class ElasticsearchFactory(NamedFactory[Elasticsearch]):
    """
    Factory for Elasticsearch clients
    """

    defaults = FACTORY_DEFAULTS
    optional_keys = FACTORY_OPTIONAL_KEYS

    def create(self, name: str = None) -> Elasticsearch:
        """
        Create an Elasticsearch client instance
        """
        config = self.get(name)
        return Elasticsearch(**config)


factory = ElasticsearchFactory("ELASTICSEARCH")
get_client = factory.create


class AsyncElasticsearchFactory(NamedFactory[AsyncElasticsearch]):
    """
    Factory for AsyncElasticsearch clients
    """

    defaults = FACTORY_DEFAULTS
    optional_keys = FACTORY_OPTIONAL_KEYS

    def create(self, name: str = None) -> AsyncElasticsearch:
        """
        Create an AsyncElasticsearch client instance
        """
        if AsyncElasticsearch:
            config = self.get(name)
            return AsyncElasticsearch(**config)
        else:
            raise RuntimeError(
                "AsyncElasticsearch is not available, install the `aiohttp` package."
            )


async_factory = AsyncElasticsearchFactory("ELASTICSEARCH")
get_async_client = async_factory.create
