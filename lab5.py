from typing import Any, Callable
from typing import Union
import matplotlib.pyplot as plt


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any, left_child=None, right_child=None):
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

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self.value)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self.value)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self.value)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def __str__(self):
        return str(self.value)


class BinaryTree:
    root: BinaryNode

    def __init__(self, root=None):
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order()

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order()


def print_node(value: Any):
    print(value)


node = BinaryNode(10, BinaryNode(9, BinaryNode(1), BinaryNode(3)), BinaryNode(2, BinaryNode(4), BinaryNode(6)))
node.traverse_in_order(print_node)
print('---------------')
node.traverse_post_order(print_node)
print('---------------')
node.traverse_pre_order(print_node)

tree = BinaryTree(node)
print('****************************')
tree.traverse_in_order(print_node)
