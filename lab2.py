from typing import Any

class Node:
    value: any
    next: 'Node'

    def __init__(self, value: Any, next=None):
        self.value = value
        self.next = None

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext


class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        current = self.head
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(value))
        else:
            self.head = Node(value)
        self.tail = current.getNext()

    def node(self, at: int):
        pointer = self.head
        counter = 0
        while True:
            if counter == at or pointer.next is None:
                return pointer
            counter += 1
            pointer = pointer.next

    def insert(self, value: Any, after: Node):
        pointer = self.head
        counter = 0
        while True:
            if counter == after:
                node = Node(value)
                node.next = pointer.next
                pointer.next = node
                return None
            if pointer.next is None:
                return
            counter += 1
            pointer = pointer.next
    def pop(self):
        pointer = self.head
        self.head = pointer.next
        return pointer
    def remove_last(self):
        pointer = self.head
        last = self.tail
        while True:
            temp = pointer.next
            if temp.value == last.value:
                break
            pointer = pointer.next
        pointer.next = None
        self.tail = pointer
    def remove(self, after: Node) -> Any:
        pointer = self.head
        while True:
            if pointer.next is after:
                pointer.next = after.next
                return None

    def len(self):
        pointer = self.head
        counter = 1
        while True:
            if pointer.next is None:
                return counter
            counter += 1
            pointer = pointer.next


lis = LinkedList()
lis.push(3)
lis.push(2)
lis.push(1)
lis.append(4)
lis.append(5)
lis.append(6)
lis.insert(23,2)
test = lis.node(0)
lis.pop()
lis.remove_last()
#lis.remove(1)
#print(test.value)
print(lis.len())