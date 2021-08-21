import requests
from LinkedList import LinkedList, Node


class LRUCache(object):
    def __init__(self, size):
        self.max_cache_size = size
        self.current_cache_size = 0
        self.key_to_object = {}
        self.list_of_items = LinkedList()

    def get(self, url):
        if self.key_to_object.get(url, None):
            # update cache: move item to head
            self.list_of_items.update_item(self.key_to_object[url])
        else:
            res = requests.get(url)
            item = Node(url, res.text)
            self.key_to_object[url] = item
            if self.current_cache_size < self.max_cache_size:
                self.list_of_items.add(item)
                self.current_cache_size += 1
            else:
                # remove least recently used item
                key_to_remove = self.list_of_items.remove_tail()
                del self.key_to_object[key_to_remove]
                self.list_of_items.add(item)


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
        lru.list_of_items.print()
        sleep(1)
