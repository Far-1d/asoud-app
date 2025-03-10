from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns(
    '',
    host(r'app', 'config.app_urls', name='app'),
    host(r'(?P<market_id>[a-zA-Z0-9-]{4,})', 'config.market_urls', name='market'),  # Dynamic pattern
    host(r'', 'config.urls', name='main'),
)
