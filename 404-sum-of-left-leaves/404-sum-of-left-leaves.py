# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
# https://leetcode.com/problems/sum-of-left-leaves/discuss/1558055/C%2B%2BPython-Recursive-and-Iterative-DFS-%2B-BFS-%2B-Morris-Traversal-O(1)-w-Explanation-or-Beats-100

# used leetcode's tree visualizer & browser inspect manipulation to create graphs. 
# There might be other tools available but this felt the simplest way to do it.

# ✔️ Solution - I (Recursive DFS)
# -------------------------------
        # def dfs(root, isLeft):
        #     if not root: return 0
        #     if not root.left and not root.right:
        #         return root.val if isLeft else 0
        #     return dfs(root.left, True) + dfs(root.right, False)
        # return dfs(root, False)
    
# ✔️ Solution - II (Iterative DFS)
# -------------------------------
        # s, ans = deque([(root, False)]), 0
        # while s:
        #     cur, isLeft = s.pop()
        #     if not cur.left and not cur.right and isLeft:
        #         ans = ans + cur.val
        #     if cur.right: 
        #         s.append((cur.right, False))
        #     if cur.left: 
        #         s.append((cur.left, True))
        # return ans

# ✔️ Solution - III (BFS)
# -------------------------------
        # q, ans = deque([(root, False)]), 0
        # while q:
        #     cur, isLeft = q.popleft()
        #     if not cur.left and not cur.right and isLeft:
        #         ans = ans + cur.val
        #     if cur.right:
        #         q.append((cur.right, False))
        #     if cur.left: 
        #         q.append((cur.left, True))
        # return ans

# ✔️ Solution - IV (Morris Traversal)
# ----------------------------------
        # ans = 0
        # while root:
        #     if root.left:
        #         pre, isLeft = root.left, True
        #         while pre.right and pre.right != root:
        #             pre = pre.right
        #         if not pre.right:
        #             pre.right = root
        #             root = root.left
        #         else:
        #             pre.right = None
        #             if pre == root.left and not pre.left:
        #                 ans = ans + pre.val
        #             root = root.right
        #     else:
        #         root = root.right
        # return ans

# -----------------------------------------------------------------------------

        if not root: return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)   # isn't leave

# -----------------------------------------------------------------------------

    # def sumOfLeftLeaves(self, root, isLeft=False):
    #     if not root: return 0
    #     if not (root.left or root.right): return root.val * isLeft
    #     return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)

        