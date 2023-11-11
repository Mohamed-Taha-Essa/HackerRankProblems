"""
earch Trees python
ChatGPT
A Binary Search Tree (BST) is a binary tree data structure with the following properties:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
The left and right subtrees are also binary search trees.
Here's a simple implementation of a Binary Search Tree in Python:


from Chatgpt
"""

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if root is None:
            return -1  # Height of an empty tree is -1

        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        return 1 + max(left_height, right_height)

from collections import deque

# def tree_height(root):
#     if root is None:
#         return -1  # Height of an empty tree is -1

#     queue = deque([(root, 0)])  # A tuple (node, level)
#     current_level = 0
    
#     print(*queue)
# myTree=Solution()

# keys = [50, 30, 70, 20, 40, 60, 80]
# root=None
# for i in keys:
#       root=myTree.insert(root,i)

# tree_height(root)
# T=int(input())
# myTree=Solution()
# root=None
# for i in range(T):
#     data=int(input())
#     root=myTree.insert(root,data)
# height=myTree.getHeight(root)
# print(height)       

from collections import deque

# Create a deque
my_deque = deque([1, 2, 3, 4, 5])

# Use popleft to remove and return the leftmost element
leftmost_element = my_deque.popleft()

print("Leftmost element:", leftmost_element)
print("Updated deque:", my_deque)
