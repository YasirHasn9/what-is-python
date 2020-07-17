'''
Doubly linked list is another type for storing data and each node of this data is
made of three parts value , next node and previous node
so each node knows what are theses things 
'''


# each node in the list should have value and 2 pointer one to prev and one to next

# class Node:
#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next


# class DLL:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             new_node.prev = None
#             self.head = new_node

#         if self.head:
#             cur = self.head
#             while cur.next:
#                 cur = cur.next
#             cur.next = new_node
#             new_node.prev = cur
#             new_node.next = None

#     def prepend(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             new_node.prev = None
#             self.head = new_node
#         else:
#             self.head.prev = new_node
#             new_node.next = self.head
#             self.head = new_node
#             new_node.prev = None

#     def remove_head(self):
#         if self.head:
#             temp = self.head
#             cur = temp.next
#             temp.prev = None
#             self.head = cur
#             return temp.data

#     def delete(self, key):
#         cur = self.head
#         while cur:

#             # check if the key is the head
#             if cur.next == key and cur == self.head:
#                 # the head is the only node in the list
#                 if not cur.next:
#                     cur = None
#                     self.head = None
#                     return

#     def print_l(self):
#         cur = self.head
#         while cur:
#             print("ggg", cur.data)
#             cur = cur.next


# dll = DLL()
# dll.append(1)
# dll.delete(1)
# dll.print_l()


# another way of writing solutions for doubly linked list

'''
each node holds a references to its next node and pervious node
as well as it value
'''


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = None
        self.prev = None

    # [a] -> <- [b] -> <- [c] -> <- [d] -> <-none
    # for instance, we want to add a new node after the b
    # so the next for the new node should the next of the b which is c
    # and the previous of c should the new node
    # and the previous of the new node should the node that
    # we want to insert after which is c
    def insert_after(self, value):
        cur_next = self.next
        self.next = ListNode(value, self, cur_next)
        if cur_next:
            cur_next.prev = self.next
