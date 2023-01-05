from typing import Any, List


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def min(self):
        current_node = self
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root):
        self.root = root

    def insert(self, value: Any) -> None:
        node = self._insert(self.root, value)
        self.root = node

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node is None:
            return BinaryNode(value)
        elif value < node.value:
            node.left_child = self._insert(node.left_child, value)
        else:
            node.right_child = self._insert(node.right_child, value)
        return node

    def insert_list(self, list_: List[Any]) -> None:
        for i in list_:
            self.insert(i)


root = BinaryNode(5)
root.left_child = BinaryNode(3)
root.right_child = BinaryNode(7)
root.left_child.left_child = BinaryNode(2)
root.left_child.right_child = BinaryNode(4)
root.right_child.left_child = BinaryNode(6)

root = BinarySearchTree(root)

root.insert(1)
