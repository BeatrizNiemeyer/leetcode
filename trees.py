# 94. Binary Tree Inorder Traversal
# Easy

# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# Example 1:

# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(root):

            if not root:
                return

            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)

        return result
