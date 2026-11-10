# LRU-Cache

A small LRU cache for HTTP GET responses, built on a doubly linked list and a dict.

```python
from lru_cache import LRUCache

cache = LRUCache(3)
body = cache.get("https://ipinfo.io/ip")  # fetched
body = cache.get("https://ipinfo.io/ip")  # served from the cache
```

When the cache is full, the least recently used URL is removed.

Requires `requests`. Run the tests with `python -m unittest`.
