from implementation.base import BaseNode


class LinkedListNode(BaseNode):
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None
        self.is_empty = True

    def add_value(self, key, value):
        if self.is_empty:
            self.key = key
            self.value = value
            self.is_empty = False
            return self

        if self.key == key:
            self.value = value
            return self

        if self.next is None:
            self.next = LinkedListNode()
            self.next.prev = self
        return self.next.add_value(key, value)

    def remove_value(self, key):
        if self.is_empty:
            raise KeyError

        if self.key == key:
            if self.next is not None:
                if self.prev is not None:
                    self.prev.next = self.next
                    self.next.prev = self.prev
                else:
                    self.key = self.next.key
                    self.value = self.next.value
                    self.prev = self.next.prev
                    self.next = self.next.next
            else:
                if self.prev is not None:
                    self.prev.next = None
                else:
                    self.value = None
                    self.key = None
                    self.is_empty = None
        else:
            if self.next is None:
                raise KeyError

            self.next.remove_value(key)

    def get_value(self, key):
        if self.is_empty:
            raise KeyError

        if self.key == key:
            return self

        if self.next is None:
            raise KeyError

        return self.next.get_value(key)

    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next
