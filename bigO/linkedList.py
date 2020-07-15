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

    def get_length(self):
        count = 0
        current_node = self.head
        while current_node:
            count = count + 1
            current_node = current_node.next
        return count

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

    def add_at_poition(self, prev_node, data):
        new_node = Node(data)

        if not prev_node:
            print("pervious not in the list")
            return

        new_node.next = prev_node.next
        prev_node.next = new_node

    def nth_position(self, data, pos):
        new_node = Node(data)

        # make 2 pointers and count
        first_p = self.head
        # should be n away from the self.head
        second_p = self.head
        count = 0

        while second_p and count < pos:
            second_p = second_p.next
            count += 1

        # the second_p is null then the position we received is greter
        # than the number in the list
        if not second_p:
            print(str(pos) + "is greater than number nodes in the list")
            return
        while first_p and second_p:
            first_p = first_p.next
            second_p = second_p.next


l_list = LinkedList()
l_list.append("a")
l_list.append("b")
l_list.append("c")
l_list.append("d")
l_list.add_at_poition(l_list.head.next, "e")
l_list.print_list()
print(l_list.get_length())


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, data):

        # 1. create new node from the value
        new_node = Node(data)

        if self.head and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # 2.set the tail's next to the new node
            self.tail.set_next(new_node)

            # 3. reassign self.tail to refer to the new Node
            self.tail = new_node
