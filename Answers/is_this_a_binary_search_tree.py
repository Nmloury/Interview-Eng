### Is This a Binary Search Tree?
### https://www.hackerrank.com/challenges/ctci-is-binary-search-tree

"""
For the purposes of this challenge, we define a binary search tree to be a binary tree with the following ordering properties:

The  value of every node in a node's left subtree is less than the data value of that node.
The  value of every node in a node's right subtree is greater than the data value of that node.
Given the root node of a binary tree, can you determine if it's also a binary search tree?

Complete the function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must return a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper functions to complete this challenge.

Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.

Input Format

You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.

Constraints

Output Format

You are not responsible for printing any output to stdout. Your function must return true if the tree is a binary search tree; otherwise, it must return false. Hidden code stubs will print this result as a Yes or No answer on a new line.
"""

### Code

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def inOrder(root, dlist=[]):
    if root.left:
        inOrder(root.left, dlist)
    dlist.append(root.data)
    if root.right:
        inOrder(root.right, dlist)
    return dlist


def isBinarySearchTree(root):
    dlist = inOrder(root)
    result = True
    for i in range(len(dlist) - 1):
        if dlist[i] >= dlist[i + 1]:
            result = False
    return result
