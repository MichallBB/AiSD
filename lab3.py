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
        while True:
            if pointer.next is None:
                return counter
            counter += 1
            pointer = pointer.next
    def test(self):
        pointer = self.head
        return pointer.next


ll = LinkedList()
print(ll)
print(ll.tail)
assert ll.head == None and ll.tail == None
ll.push(1)
print(ll)
print(ll.tail.value)
ll.push(0)
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))
assert str(ll) == '0 -> 1'
assert ll.tail.value == 1

ll.append(9)
ll.append(10)
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))
assert str(ll) == '0 -> 1 -> 9 -> 10';
assert ll.tail.value == 10

ltmp = LinkedList()
ltmp.push(11)
print(str(ltmp) + "; ogona_wartosc=" + str(ltmp.tail.value))
ltmp = None

print("----------------")
middle_node = ll.node(at=1)
print(middle_node.value)
assert (middle_node.value == 1)
ll.insert(5, after=middle_node)
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))
assert str(ll) == '0 -> 1 -> 5 -> 9 -> 10'

print("")
ltmp = LinkedList()
ltmp.push(11)
ltmp.insert(15, after=ltmp.node(at=0))
print(str(ltmp) + "; ogona_wartosc=" + str(ltmp.tail.value))
assert (str(ltmp) == "11 -> 15")
assert (ltmp.tail.value == 15)
ltmp = None

print("")
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))
first_element = ll.node(at=0)
returned_first_element_val = ll.pop()
print(returned_first_element_val)
assert first_element.value == returned_first_element_val.value
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))

print('test pop')
ltmp = LinkedList()
ltmp.push(31)
print(ltmp.pop())
print(str(ltmp))
ltmp = None

last_element = ll.node(at=3)
returned_last_element_val = ll.remove_last()
assert last_element.value == returned_last_element_val.value
assert str(ll) == '1 -> 5 -> 9'
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))

print("")
ltmp = LinkedList()
ltmp.push(41)
returned_last_element_val = ltmp.remove_last()
print(returned_last_element_val)
assert (returned_last_element_val.value == 41)
assert (ltmp.tail == None)
print(str(ltmp))
ltmp = None

#------------------------------------------------------
print("")
second_node = ll.node(at=1)
ll.remove(second_node)
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))
assert str(ll) == '1 -> 5'
assert (ll.tail.value == 5)

print("")
ltmp = LinkedList()
ltmp.push(41)
print(ltmp.remove_last())
print(ltmp)
assert (ltmp.head == None and ltmp.tail == None)
ltmp = None

ll = None
ll = LinkedList()
ll.append(0)
ll.append(1)
ll.append(1)
ll.append(9)
ll.append(10)
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))
assert str(ll) == '0 -> 1 -> 9 -> 10';
assert ll.tail.value == 10

ltmp = LinkedList()
ltmp.push(11)
print(str(ltmp) + "; ogona_wartosc=" + str(ltmp.tail.value))
ltmp = None

print("")
middle_node = ll.node(at=1)
print(middle_node.value)
assert (middle_node.value == 1)
ll.insert(5, after=middle_node)
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))
assert str(ll) == '0 -> 1 -> 5 -> 9 -> 10'

print("")
ltmp = LinkedList()
ltmp.push(11)
ltmp.insert(15, after=ltmp.node(at=0))
print(str(ltmp) + "; ogona_wartosc=" + str(ltmp.tail.value))
assert (str(ltmp) == "11 -> 15")
assert (ltmp.tail.value == 15)
ltmp = None

print("")
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))
first_element = ll.node(at=0)
returned_first_element_val = ll.pop()
print(returned_first_element_val)
assert first_element.value == returned_first_element_val.value
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))

ltmp = LinkedList()
ltmp.push(31)
print(ltmp.pop())
print(str(ltmp))
ltmp = None

last_element = ll.node(at=3)
returned_last_element_val = ll.remove_last()
assert last_element.value == returned_last_element_val.value
assert str(ll) == '1 -> 5 -> 9'
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))

print("")
ltmp = LinkedList()
ltmp.push(41)
returned_last_element_val = ltmp.remove_last()
print(returned_last_element_val)
assert (returned_last_element_val.value == 41)
assert (ltmp.tail == None)
print(str(ltmp))
ltmp = None

print("")
second_node = ll.node(at=1)
ll.remove(second_node)
print(str(ll) + "; ogona_wartosc=" + str(ll.tail.value))
assert str(ll) == '1 -> 5'
assert (ll.tail.value == 5)

print("")
ltmp = LinkedList()
ltmp.push(41)
print(ltmp.remove_last())
print(ltmp)
assert (ltmp.head == None and ltmp.tail == None)
ltmp = None

ll = None