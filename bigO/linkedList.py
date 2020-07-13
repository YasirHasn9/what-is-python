# Linked List
'''
The main difference between normal list and linked list and that each 
item in the list treated as an isolated node 

each node made of value and a pointer to the next node
'''


class Node:
    def __init__(self, value, next_node=None):
        '''
        each node in the list can not refere to the pervious node 
        but it can refere to next node
        '''
        self.value = value
        self.next = next_node


'''
The linked list contains several items first item of the list called the head
and the last node called the tail
to make sure that we have the tail then it should pointed to None
'''


class LinkedList:
    '''
    in linked list if you want to access to a certain node in the list 
    you have to go through the head through each node before that node
    '''
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


