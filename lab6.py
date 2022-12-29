from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value, left_child=None, right_child=None):
        self.left_child = left_child
        self.right_child = right_child
        self.value = value

    def is_leaf(self):
        if (self.right_child == None and self.left_child == None):
            return True
        return False

    def add_left_child(self, value: Any):
        if self.left_child is None:
            self.left_child = value

    def add_right_child(self, value: Any):
        if self.right_child is None:
            self.right_child = value

    def __str__(self):
        return self.value

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_in_order()
        print(self.value)
        if self.right_child != None:
            self.right_child.traverse_in_order()


class BinaryTree:
    root: BinaryNode

    def __init__(self, root):
        self.root = root


A = BinaryNode(10)
B = BinaryNode(9)
C = BinaryNode(2)
D = BinaryNode(4)
E = BinaryNode(6)
F = BinaryNode(1)
G = BinaryNode(3)

A.add_right_child(C)
A.add_left_child(B)
B.add_left_child(F)
B.add_right_child(G)
C.add_left_child(D)
C.add_right_child(E)



print(D.is_leaf())