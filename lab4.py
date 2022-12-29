from typing import Any, Callable, Union

class TreeNode:
    def __init__(self, value: Any):
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def add(self, child: 'TreeNode'):
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]):
        visit(self)
        for child in self.children:
            child.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]):
        queue = [self]
        while queue:
            node = queue.pop(0)
            visit(node)
            queue.extend(node.children)

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        for child in self.children:
            result = child.search(value)
            if result is not None:
                return result
        return None

    def __str__(self):
        return str(self.value)