import unittest
from unittest import mock

from LinkedList import LinkedList, Node
from lru_cache import LRUCache


def fake_get(url, timeout=None):
    res = mock.Mock(text="body of " + url)
    res.raise_for_status.return_value = None
    return res


def keys(cache):
    forward = [n.key for n in cache.list_of_items]
    backward = []
    node = cache.list_of_items.tail
    while node:
        backward.append(node.key)
        node = node.prev
    assert forward == backward[::-1], (forward, backward)
    return forward


@mock.patch("lru_cache.requests.get", side_effect=fake_get)
class LRUCacheTest(unittest.TestCase):
    def test_get_returns_value(self, get):
        cache = LRUCache(2)
        self.assertEqual(cache.get("a"), "body of a")
        self.assertEqual(cache.get("a"), "body of a")
        self.assertEqual(get.call_count, 1)

    def test_evicts_least_recently_used(self, get):
        cache = LRUCache(3)
        for k in "abc":
            cache.get(k)
        cache.get("b")  # move a middle item to the head
        cache.get("d")  # evicts a
        self.assertEqual(keys(cache), ["d", "b", "c"])
        self.assertEqual(sorted(cache.key_to_object), ["b", "c", "d"])

    def test_size_one(self, get):
        cache = LRUCache(1)
        cache.get("a")
        cache.get("b")
        self.assertEqual(keys(cache), ["b"])
        self.assertEqual(list(cache.key_to_object), ["b"])

    def test_move_tail_to_head(self, get):
        cache = LRUCache(3)
        for k in "abc":
            cache.get(k)
        cache.get("a")
        self.assertEqual(keys(cache), ["a", "c", "b"])

    def test_invalid_size(self, get):
        with self.assertRaises(ValueError):
            LRUCache(0)


class LinkedListTest(unittest.TestCase):
    def test_remove_tail_until_empty(self):
        ll = LinkedList()
        ll.add(Node(1, "x"))
        ll.add(Node(2, "y"))
        self.assertEqual(ll.remove_tail(), 1)
        self.assertEqual(ll.remove_tail(), 2)
        self.assertIsNone(ll.remove_tail())
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)


if __name__ == "__main__":
    unittest.main()
