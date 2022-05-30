# https://leetcode.com/problems/find-the-difference/discuss/1751380/JavaC%2B%2BPython-very-very-EASY-to-go-solution

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # l = list(t)
        # for char in list(s):
        #     l.remove(char)      
        # return l[0]
    
# ---------------------------------------------------------------                
    
        # c = 0
        # for cs in s: c ^= ord(cs) #ord is ASCII value
        # for ct in t: c ^= ord(ct)
        # return chr(c) #chr = convert ASCII into character
            
# ---------------------------------------------------------------   
        # return chr(reduce(lambda x,y: x ^ y, map(ord,s+t)))
# --------------------------------------------------------------- 
# Dictionary
# -----------
        # dic = {}
        # for ch in s:
        #     dic[ch] = dic.get(ch, 0) + 1
        # for ch in t:
        #     if dic.get(ch, 0) == 0:
        #         return ch
        #     else:
        #         dic[ch] -= 1
# ---------------------------------------------------------------                
# Difference
# -----------
        # diff = 0
        # for i in range(len(s)):
        #     diff -= ord(s[i])
        #     diff += ord(t[i])
        # diff += ord(t[-1])
        # return chr(diff)
# ---------------------------------------------------------------                
# XOR
# -----------
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)
# ---------------------------------------------------------------                
        
# Wrong Answer: "a", "aa"
# ---------------------------
        # for char in t:
        #     if char not in s:
        #         return char
        