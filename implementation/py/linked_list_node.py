from typing import Any

from implementation.py.base import BaseNode


class LinkedListNode(BaseNode):
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None
        self.is_empty = True

    def add_value(self, key: Any, value: Any) -> "LinkedListNode":
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

    def get_node(self, key: Any) -> "LinkedListNode":
        if self.is_empty:
            raise KeyError

        if self.key == key:
            return self

        if self.next is None:
            raise KeyError

        return self.next.get_node(key)

    def remove_value(self, key: Any) -> None:
        node = self.get_node(key)
        if node.next is not None:
            if node.prev is not None:
                node.prev.next = node.next
                node.next.prev = node.prev
            else:
                node.key = node.next.key
                node.value = node.next.value
                node.prev = node.next.prev
                node.next = node.next.next
        else:
            if node.prev is not None:
                node.prev.next = None
            else:
                node.value = None
                node.key = None
                node.is_empty = None

    def get_value(self, key: Any) -> Any:
        return self.get_node(key).value

    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next
