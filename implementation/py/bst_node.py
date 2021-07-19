from implementation.py.base import BaseNode


class BSTNode(BaseNode):
    def __init__(self):
        self.key = None
        self.value = None
        self.left = None
        self.right = None
        self.parent = None
        self.direction = None
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

        if self.key > key:
            if self.left is None:
                self.left = BSTNode()
                self.left.parent = self
                self.left.direction = "LEFT"
            return self.left.add_value(key, value)

        else:
            if self.right is None:
                self.right = BSTNode()
                self.right.parent = self
                self.right.direction = "RIGHT"
            return self.right.add_value(key, value)

    def get_node(self, key):
        if self.is_empty:
            raise KeyError

        if self.key == key:
            return self

        if self.key > key:
            if self.left is None:
                raise KeyError
            return self.left.get_node(key)
        else:
            if self.right is None:
                raise KeyError
            return self.right.get_node(key)

    def get_value(self, key):
        node = self.get_node(key)
        return node.value

    @staticmethod
    def min_tree_value(node):
        while node.left is not None:
            node = node.left
        return node

    @staticmethod
    def _remove_node(node):
        if node.left is None and node.right is None:
            if node.parent is None:
                node.is_empty = True
                node.key = None
                node.value = None
            else:
                if node.direction == "LEFT":
                    node.parent.left = None
                else:
                    node.parent.right = None

        elif node.left is None:
            node.key = node.right.key
            node.value = node.right.value
            node.left = node.right.left
            node.right = node.right.right

        elif node.right is None:
            node.key = node.left.key
            node.value = node.left.value
            node.right = node.left.right
            node.left = node.left.left

        else:
            min_node = BSTNode.min_tree_value(node.right)
            node.key = min_node.key
            node.value = min_node.value
            BSTNode._remove_node(min_node)

    def remove_value(self, key):
        node = self.get_node(key)
        self._remove_node(node)

    def __iter__(self):
        node = self
        nodes = []
        while nodes or node:
            if node:
                nodes.append(node)
                node = node.right
            else:
                node = nodes.pop(-1)
                yield node
                node = node.left
