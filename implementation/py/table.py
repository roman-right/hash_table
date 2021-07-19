from typing import Any, List

from implementation.py.base import BaseHashTable
from implementation.py.node import LinkedListNode


class HashTable(BaseHashTable):
    def __init__(self, size: int = 8, max_load_factor: float = 1):
        self.size = size
        self.load = 0
        self.max_load_factor = max_load_factor
        self.array: List[LinkedListNode] = [LinkedListNode() for _ in
                                            range(self.size)]

    @property
    def load_factor(self):
        return self.load / self.size

    def _hash(self, key: int):
        if not isinstance(key, int):
            raise TypeError("key must be of type int")
        return key % self.size

    def __setitem__(self, key: int, value: Any):
        node_index = self._hash(key)
        self.array[node_index].add_value(key, value)
        self.load += 1
        if self.load_factor >= self.max_load_factor:
            self._resize()

    def __getitem__(self, item):
        node_index = self._hash(item)
        return self.array[node_index].get_value(item)

    def __delitem__(self, key):
        node_index = self._hash(key)
        self.array[node_index].remove_value(key)
        self.load -= 1

    def _resize(self):
        new_table = HashTable(size=self.size * 2,
                              max_load_factor=self.max_load_factor)
        for node in self.array:
            if not node.is_empty:
                for element in node:
                    new_table[element.key] = element.value

        self.size = new_table.size
        self.load = new_table.load
        self.array = new_table.array
