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

    def remove_head(self):
        if self.head:
            temp = self.head
            cur = temp.next
            temp.prev = None
            self.head = cur
            return temp.data

    def delete(self, key):
        cur = self.head
        while cur:

            # check if the key is the head
            if cur.next == key and cur == self.head:
                # the head is the only node in the list
                if not cur.next:
                    cur = None
                    self.head = None
                    return

    def print_l(self):
        cur = self.head
        while cur:
            print("ggg", cur.data)
            cur = cur.next


dll = DLL()
dll.append(1)
dll.delete(1)
dll.print_l()

# def delete(self, key):
#     cur = self.head
#     while cur:
#         # if the node that we want to delete heppens to be the first node(head) of list
#         if cur.next == key and cur == self.head:
#             # if the node is the only node in the list
#             if not cur.next:
#                 cur = None
#                 self.head = None
#                 return cur.data
#             else:
#                 # get the node after the cur
#                 nxt = cur.next
#                 # the pervious node of the next should none
#                 nxt.prev = None
#                 # make the deleted node none
#                 cur = None
#                 self.head = nxt
#                 return
#         elif cur.data == key:
#             if cur.next:
#                 nxt = cur.next
#                 prev = cur.prev
#                 prev.next = nxt
#                 nxt.prev = prev
#                 cur.next = None
#                 cur.prev = None
#                 cur = None
#                 return
#             else:
#                 prev = cur.prev
#                 prev.next = None
#                 cur.prev = None
#                 cur = None
#                 return
#         cur = cur.next
