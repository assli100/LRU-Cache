class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, item):
        if self.head:
            self.head.prev = item
            item.next = self.head
        else:
            self.tail = item
        self.head = item

    def update_item(self, item):
        if item == self.head:
            return
        if item == self.tail:
            self.tail = item.prev
        item.prev.next = item.next
        self.add(item)

    def remove_tail(self):
        if not self.tail:
            return
        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        key = temp.key
        del temp
        return key

    def print(self):
        res = ""
        temp = self.head
        while temp:
            res += "{} --> ".format(temp.value.strip())
            temp = temp.next
        res += "null"
        print(res)

    def reverse_print(self):
        res = ""
        temp = self.tail
        while temp:
            res += "{} --> ".format(temp.value)
            temp = temp.prev
        res += "null"
        print(res)


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add(Node(4))
    linked_list.add(Node(3))
    linked_list.add(Node(5))
    linked_list.print()
    linked_list.reverse_print()

