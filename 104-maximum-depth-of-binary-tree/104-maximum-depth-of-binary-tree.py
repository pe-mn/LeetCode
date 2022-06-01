# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
# RECURSIVE DFS 
# -------------
# To calculate the maximum depth we can use the Depth-First Search. We call a helper function recursively and return the maximum depth between left and right branches.

#         def dfs(root, depth):
#             if not root: return depth
#             return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
#         return dfs(root, 0)
    
# ---------------------------------------------------------------------------  
# It can be written more simply:
# ------------------------------
# https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/359949/Python-recursive-and-iterative-solution

        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
# The idea is we start from the top of the tree. Each node adds one level of depth to the subtree rooted at its left and right child. The maximum depth of the tree rooted at the current node is the maximum depth of the tree rooted at the left and right child + 1. The base case for our recursion is when we hit an empty child who does not contribute to increasing the depth of the tree and therefore it's maximum depth is 0.

# self. maxDepth(None) = 0 by definition

# self. maxDepth(10)
# max(self. maxDepth(5), self. maxDepth(19)) + 1 # First recursive call from node 10
# max(max(self. maxDepth(None), self. maxDepth(None)) + 1, self. maxDepth(19)) + 1  # Recursive call on node 5 and its expansion
# max(1, self. maxDepth(19)) + 1 # Replacing for self. maxDepth(None) = 0 
# max(1, max(self. maxDepth(17), self. maxDepth(None)) + 1) + 1 # Recursive call from node 19
# max(1, max(self. maxDepth(17), 0) + 1) + 1 # Replacing for self. maxDepth(None) = 0 
# max(1, max(max(self. maxDepth(None), self. maxDepth(None)) + 1, 0) + 1) + 1 # Recursive call from node 17
# max(1, max(max(0, 0) + 1, 0) + 1) + 1 # Replacing for self. maxDepth(None) = 0
# max(1, max(0 + 1, 0) + 1) + 1 # Replacing the inner most max
# max(1, 1 + 1) + 1 # Replacing the inner most max
# max(1, 2) + 1
# 2 + 1 # Replacing the inner most max
# 3
        