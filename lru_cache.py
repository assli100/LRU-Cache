import requests
from LinkedList import LinkedList, Node

REQUEST_TIMEOUT = 10  # seconds


class LRUCache(object):
    def __init__(self, size):
        if size < 1:
            raise ValueError("cache size must be at least 1")
        self.max_cache_size = size
        self.key_to_object = {}
        self.list_of_items = LinkedList()

    def get(self, url):
        """Return the page body for url, fetching it if it is not cached."""
        item = self.key_to_object.get(url)
        if item is not None:
            # cache hit: mark as most recently used
            self.list_of_items.update_item(item)
            return item.value

        res = requests.get(url, timeout=REQUEST_TIMEOUT)
        # don't cache error responses
        res.raise_for_status()

        if len(self.key_to_object) >= self.max_cache_size:
            # remove least recently used item
            key_to_remove = self.list_of_items.remove_tail()
            del self.key_to_object[key_to_remove]

        item = Node(url, res.text)
        self.key_to_object[url] = item
        self.list_of_items.add(item)
        return item.value


if __name__ == "__main__":
    from random import randint
    from time import sleep
    lru = LRUCache(3)
    base_url = "https://ipinfo.io/"
    urls = ["ip", "city", "country", "timezone", "org", "loc"]
    while True:
        i = randint(0, 5)
        url = base_url + urls[i]
        lru.get(url)
        print(" --> ".join(node.key for node in lru.list_of_items))
        sleep(1)
