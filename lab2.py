from typing import Any


class Node:
    value: any
    next: 'Node'

    def __init__(self, value: Any, next=None):
        self.value = value
        self.next = next

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

    def __str__(self):
        text = ''
        current = self.head
        if current != None:
            text += str(current.value)
            current = current.next
            while current.next != None:
                current = current.next
                text += " -> " + str(current.value)
        return text

    def push(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = Node(value)
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, value):
        current = self.head
        if current:
            while current.next != None:
                current = current.next
            current.setNext(Node(value))
        else:
            self.head = Node(value)
            current = self.head
        self.tail = current.next

    def node(self, at: int):
        pointer = self.head
        counter = 0
        if at == 0:
            return pointer
        while counter < at:
            pointer = pointer.next
            counter += 1
        return pointer.next

    def insert(self, value: Any, after: Node):
        nnode = Node(value)
        pointer = after
        if self.head == after:
            pointer = after.next
        if pointer.next == None:
            self.tail = nnode
        nnode.next = pointer.next
        pointer.next = nnode

    def pop(self):
        pointer = self.head
        if self.tail == pointer.next:
            self.head = None
            self.tail = None
        else:
            self.head = pointer.next
            return pointer

    def remove_last(self):
        pointer = self.head
        last = self.tail
        if self.tail == pointer.next:
            temp = pointer.next
            self.head = None
            self.tail = None
            return temp
        else:
            while True:
                temp = pointer.next
                if temp.value == last.value:
                    break
                pointer = pointer.next
            temp = pointer.next
            pointer.next = None
            self.tail = pointer
            return temp

    def remove(self, after: Node) -> Any:
        pointer = after.next
        if pointer.next == None:
            self.tail = after
            after.next = None
            return
        pointer = pointer.next
        after.next = pointer
        return

    def len(self):
        pointer = self.head
        counter = 1
        if self.head is None:
            return 0
        while True:
            if pointer.next is None:
                return counter
            counter += 1
            pointer = pointer.next

    def test(self):
        pointer = self.head
        return pointer.next


# LIFO
class Stack:
    def __init__(self):
        self._storage = LinkedList()

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def pop(self) -> Any:
        return self._storage.pop().value

    def __len__(self):
        return self._storage.len()

# FIFO
class Queue:
    def __init__(self):
        self._storage = LinkedList()

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop().value

    def __len__(self):
        return self._storage.len()

# LIFO
stack = Stack()
assert len(stack) == 0
stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3
top_value = stack.pop()
assert top_value == 1
assert len(stack) == 2

# FIFO
queue = Queue()
assert len(queue) == 0
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'
client_first = queue.dequeue()
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
