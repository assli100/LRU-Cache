class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LinkedList(object):
    """Doubly linked list. The head is the most recently used item."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        item.prev = None
        item.next = self.head
        if self.head:
            self.head.prev = item
        else:
            self.tail = item
        self.head = item

    def _unlink(self, item):
        if item.prev:
            item.prev.next = item.next
        else:
            self.head = item.next
        if item.next:
            item.next.prev = item.prev
        else:
            self.tail = item.prev
        item.prev = item.next = None

    def update_item(self, item):
        """Move an item that is already in the list to the head."""
        if item is self.head:
            return
        self._unlink(item)
        self.add(item)

    def remove_tail(self):
        """Remove the tail and return its key, or None if the list is empty."""
        if not self.tail:
            return None
        item = self.tail
        self._unlink(item)
        return item.key

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def print(self):
        print(" --> ".join([str(node.value) for node in self] + ["null"]))

    def reverse_print(self):
        values = []
        node = self.tail
        while node:
            values.append(str(node.value))
            node = node.prev
        print(" --> ".join(values + ["null"]))


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add(Node(4, "four"))
    linked_list.add(Node(3, "three"))
    linked_list.add(Node(5, "five"))
    linked_list.print()
    linked_list.reverse_print()
