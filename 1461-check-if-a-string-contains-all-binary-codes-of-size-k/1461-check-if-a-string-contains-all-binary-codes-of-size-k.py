import itertools
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # def foo(s):
        #     yield from itertools.product(*([set(s)] * k))
        # for comb in foo(s):
        #     if ''.join(comb) not in s: 
        #         return False
        # return True       
# --------------------------------------------------------------- 
# Wrong Answer 
# Input "1", 1
# Output true, Expected false
# ---------------------------
        # for comb in itertools.product(set(s), repeat=k):   
        #     if ''.join(comb) not in s: 
        #         return False
        # return True
# ---------------------------------------------------------------
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/discuss/2092441/Python-oror-2-Easy-oror-One-liner-with-explanation

# when k = 2, then number of combinations is 2^k = 4 i.e {'00', '11', '01', '10'}

        # return len({s[i:i+k] for i in range(len(s)-k+1)}) == 2 ** k  

# The above code requires to find all the possible combinations in input s first before comparing with required count. This can be improved a bit more with the following approach which will kill the loop once it meets the required count:
    
        n=len(s)
        required_count=2 ** k        
        seen=set()
        for i in range(n-k+1):
            tmp=s[i:i+k]
            if tmp not in seen:
                seen.add(tmp)
                required_count-=1
                if required_count==0: # kill the loop once the condition is met
                    return True
        return False 
    
# ---------------------------------------------------------------
        # return len({s[i - k : i] for i in range(k, len(s) + 1)}) == 1 << k
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