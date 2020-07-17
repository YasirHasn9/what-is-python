'''

You can think of tree as linked list without of the constrains of having each node
points to another node where in trees each node could points to 2 nodes at most
                     * root 
                    / \
                   *   * parent
                      / \
                    *    * children 
                  /  \  
                 *    * leaf


[root] is the top most node.
[child] is the node that directly connected to other node when moving away from 
the root node.
[parent] is the node that directely connected to another node when moving towards 
the parent
[siblings ] nodes that share the same parent
[leaf] node that has no children



Binary search for any given node , all the values on the left subtree are less than 
the given node and the node on the right are bigger that the given node
2 children left node and right node
left node is smaller than the parent and the right one is greater than the parent


class BinarySearchTree:
    def __init__(self):
        self.value = Value
        self.left = left_subtree
        self.right = right_subtree


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
