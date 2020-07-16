# Binary Search

'''
Binary search a tree of data structure in which each node has at most
2 children left node and right node
left node is smaller than the parent and the right one is greater than the parent


to say this tree is full then the nodes should have 2 child

                     *
                    / \
                   *   *
                      / \
                    *    *
                  /  \  
                 *    * 

    so the child either should have 2 child or none



to say this is tree is complete
                     
                       * 
                      / \
                    /    \
                   *       *
                 /   \    / \
                *      *  *  *
                     / \
                    *   *         
so one of the node is having only one node
so if there is one node in the last level should on the left side



to say this tree is perfect where all the leafs on the same level
                       * 
                     /     \
                   *         *
                  /  \      /  \
                *      *   *     *



There are 3 ways to traverse binary tree
preorder traversal N L R node left and right
in Order traversal L N R left node and right
post travesal      L R N left right and node


and all of them we categorized them under the concept of 
       Depth_first traversal
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearch(object):
    def __init__(self, root):
        self.root = Node(root)


tree = BinarySearch(1)
tree.root.left(2)
tree.root.right(3)
