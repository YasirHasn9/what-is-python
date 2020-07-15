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
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node

    def print_l(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
dll = DLL()
dll.append(1)
dll.print_l()
