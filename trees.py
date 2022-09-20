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


# 104. Maximum Depth of Binary Tree
# Easy

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

def maxDepth(root):

    # Recursion

    # if not root:
    #     return 0

    # return 1 + max(self.maxDepth(root.left) , self.maxDepth(root.right))

    # BFS

    # count = 0
    # q = deque([root])

    # while q:

    #     for i in range(len(q)):
    #         node = q.popleft()
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)
    #     count+=1

    # return count

    # DFS

    stack = [[root, 1]]
    count = 0

    while stack:
        node, depth = stack.pop()

        if node:
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
            count = max(count, depth)

    return count
