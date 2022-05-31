import itertools
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # def foo(s):
        #     yield from itertools.product(*([set(s)] * k))
        # for comb in foo(s):
        #     if ''.join(comb) not in s: 
        #         return False
        # return True
        
        
#         for comb in itertools.product(set(s), repeat=k):   
#             if ''.join(comb) not in s: 
#                 return False
#         return True
# ---------------------------------------------------------------
        return len({s[i - k : i] for i in range(k, len(s) + 1)}) == 1 << k
# ---------------------------------------------------------------
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/discuss/660829/Python-1-line-Follow-Up

        # return len({s[i:i + k] for i in range(len(s) - k + 1)}) == 2 ** k

# The problem should be:
# Given a binary string s and an integer k.
# Return True if all binary code of length k is a substring of s. Otherwise, return False.

# That's easy warm-up.
# Then here come the my question.

# Given a binary string s and an integer k.
# Return True if all binary code of length k is a subsequence of s. Otherwise, return False.

# The difficult will be doubled,
# so it 2 lines solution is acceptable to solve in python.