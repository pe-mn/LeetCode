# https://leetcode.com/problems/binary-tree-cameras/discuss/211180/JavaC%2B%2BPython-Greedy-DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:        
# Greedy DFS
# ------------
        self.res = 0
        def dfs(root):
            if not root: return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            return 2 if l == 1 or r == 1 else 0
        return (dfs(root) == 0) + self.res
    
    
# Intuition:
# Consider a node in the tree.
# It can be covered by its parent, itself, its two children.
# Four options.

# Consider the root of the tree.
# It can be covered by left child, or right child, or itself.
# Three options.

# Consider one leaf of the tree.
# It can be covered by its parent or by itself.
# Two options.

# If we set a camera at the leaf, the camera can cover the leaf and its parent.
# If we set a camera at its parent, the camera can cover the leaf, its parent and its sibling.

# We can see that the second plan is always better than the first.
# Now we have only one option, set up camera to all leaves' parent.

# Here is our greedy solution:

# Set cameras on all leaves' parents, thenremove all covered nodes.
# Repeat step 1 until all nodes are covered.
# Explanation:
# Apply a recusion function dfs.
# Return 0 if it's a leaf.
# Return 1 if it's a parent of a leaf, with a camera on this node.
# Return 2 if it's coverd, without a camera on this node.

# For each node,
# if it has a child, which is leaf (node 0), then it needs camera.
# if it has a child, which is the parent of a leaf (node 1), then it's covered.

# If it needs camera, then res++ and we return 1.
# If it's covered, we return 2.
# Otherwise, we return 0.