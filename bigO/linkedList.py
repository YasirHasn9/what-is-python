# Linked List
'''
The main difference between normal list and linked list and that each 
item in the list treated as an isolated node 

each node made of value and a pointer to the next node
'''
'''

class Node:
    def __init__(self, value, next_node=None):
    
        # each node in the list can not refere to the pervious node 
        # but it can refere to next node
    
        self.value = value
        # this points to the next node in the list
        self.next = next_node

The linked list contains several items first item of the list called the head
and the last node called the tail
to make sure that we have the tail then it should pointed to None



class LinkedList:

    # in linked list if you want to access to a certain node in the list 
    # you have to go through the head through each node before that node
    

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

Linked list represent the item in recursive way while the arrays in iterative

insertion is O(1)
accessing is O(n)
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        current_node = self.head
        new_node.next = current_node
        self.head = new_node


l_list = LinkedList()
l_list.append("a")
l_list.append("b")
l_list.prepend("c")
l_list.print_list()
