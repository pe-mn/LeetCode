class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l = list(t)
        for char in list(s):
            l.remove(char)      
        return l[0]
            
# ---------------------------------------------------------------                
        
# Wrong Answer: "a", "aa"
# ---------------------------
        # for char in t:
        #     if char not in s:
        #         return char
        