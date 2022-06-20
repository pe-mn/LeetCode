class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:    
# Explanation of solution
# Base on @awice's idea. This solution is not my intuition but it is really simple to write, compared with Trie solution.

# Build a set of words.
# Iterate on all words and remove all suffixes of every word from the set.
# Finally the set will the set of all encoding words.
# Iterate on the set and return sum(word's length + 1 for every word in the set)

        # s = set(words)
        # for w in words:
        #     for i in range(1, len(w)):
        #         s.discard(w[i:])
        # return sum(len(w) + 1 for w in s)
        
# Trie Solution
# ----------------
        root = dict()
        leaves = []
        for word in set(words):
            cur = root
            for i in word[::-1]:
                cur[i] = cur = cur.get(i, dict())
            leaves.append((cur, len(word) + 1))
        return sum(depth for node, depth in leaves if len(node) == 0)
    
                                  
# Wrong Answer
# ["me","time"]
# ["time","time","time","time"]
# Time Limit Exceeded
# ------------------------------
#         if len(words) == 1:
#             return len(words[0])+1
        
#         # remove duplicates
#         words = list(set(words))
        
#         res = 0  
#         for i in range(len(words)):
#             if any(word.endswith(words[i]) for word in words if len(words[i]) < len(word)):
#                 continue
#             else:
#                 res += len(words[i]) + 1  # to account for the #                
#         return res
                
                
        