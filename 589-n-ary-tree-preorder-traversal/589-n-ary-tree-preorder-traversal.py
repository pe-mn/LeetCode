# https://stackoverflow.com/questions/52483521/split-list-at-a-specific-value

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):

# Python short iterative solution beats 100% // 66 ms faster than fastest !
# --------------------------------------------------------------------------
        # ret, q = [], root and [root]
        # while q:
        #     node = q.pop()
        #     ret.append(node.val)
        #     q += [child for child in reversed(node.children) if child]
        # return ret 
        
# Nice but reversed function is much faster than [::-1], and is more explicit:

# -----------------------------------------------------------------------

# [Python] iterative solution, explained
# ---------------------------------------

# In this problem we just need to do what is asked: preordrer traversal. Create stack, where we put root of out tree. Then on each step we extract last element from stack, add it to out and then traverse all children. Note, that we need to traverse children in the reversed order, similar to what we did for binary tree, where we traversed first right and then left.

        if not root: return []
        stack, out = [root], []
        while stack:
            cur = stack.pop()
            out.append(cur.val)
            # for child in cur.children[::-1]:
            #     stack += [child]
            stack.extend(reversed(cur.children))
        return out
    
# I think the code will be cleaner if the last for loop is changed to stack.extend(cur.children[::-1])

        # stack,s=[root],[]
        # while stack:
        #     p=stack.pop()
        #     if p:
        #         s.append(p.val)
        #         for i in range(len(p.children)-1,-1,-1): stack.append(p.children[i])
        # return s
    
# - Since only the left side was used, it could be replaced by stack.
# - Besides, space complexity of "node.children[::-1]" is the max length of all node.children. It could potentially be space-consuming, when some nodes have long .children.

# -----------------------------------------------------------------------
     
        
        