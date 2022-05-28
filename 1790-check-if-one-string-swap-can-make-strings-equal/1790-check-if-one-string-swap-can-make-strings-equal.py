class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:       
#         if s1 == s2: # i.e diff = 0
#             return True
        
#         if sorted(s1) != sorted(s2):
#             return False
        
#         diff = 0
#         for i, j in zip(s1, s2):
#             if i != j:
#                 diff += 1
                
#         return True if diff == 2 else False

# -----------------------------------------------------------------------

# sorted(s1)==sorted(s2) is having TC: O(NlogN). Here is a similar approach for O(N)

        count = 0
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2: count += 1
        return (Counter(s1) == Counter(s2)) and (count == 0 or count == 2)
    
# -----------------------------------------------------------------------
        
        # diff = [[x, y] for x, y in zip(s1, s2) if x != y]
        # return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]
        
        