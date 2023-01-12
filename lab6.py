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

    # która sprawdzi czy w drzewie znajduje się węzeł o wskazanej wartości
    def contains(self, value: Any) -> bool:
        current_node = self.root
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left_child
            elif value > current_node.value:
                current_node = current_node.right_child
            elif value == current_node.value:
                return True
        return False

    def remove(self, value: Any) -> None:
        self.root = self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node is None:
            return None
        elif value < node.value:
            node.left_child = self._remove(node.left_child, value)
        elif value > node.value:
            node.right_child = self._remove(node.right_child, value)
        else:
            if node.left_child is None and node.right_child is None:
                node = None
            elif node.left_child is None:
                node = node.right_child
            elif node.right_child is None:
                node = node.left_child
            else:
                node_replacement = node.right_child
                while node_replacement.left_child is not None:
                    node_replacement = node_replacement.left_child
                node.value = node_replacement.value
                node.right_child = self._remove(node.right_child, node_replacement.value)
        return node


node = BinaryNode(5)
node.left_child = BinaryNode(3)
node.right_child = BinaryNode(7)
node.left_child.left_child = BinaryNode(2)
node.left_child.right_child = BinaryNode(4)
node.right_child.left_child = BinaryNode(6)

root = BinarySearchTree(node)

min = node.min()
print(min)

root.insert(9)
root.insert(7)
print(root.contains(55))
#root.remove(5)
