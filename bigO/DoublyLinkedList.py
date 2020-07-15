'''
Doubly linked list is another type for storing data and each node of this data is
made of three parts value , next node and previous node
so each node knows what are theses things 
'''


# each node in the list should have value and 2 pointer one to prev and one to next

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DLL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node

        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_l(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


dll = DLL()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.print_l()
