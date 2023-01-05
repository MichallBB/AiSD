from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any, left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def is_leaf(self):
        if self.left_child and self.right_child is None:
            return True
        return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)


class BinaryTree:
    root: BinaryNode