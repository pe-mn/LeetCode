class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:       
        if s1 == s2:
            return True
        
        if sorted(s1) != sorted(s2):
            return False
        
        diff = 0
        for i, j in zip(s1, s2):
            if i != j:
                diff += 1
                
        return True if diff <= 2 else False
                
        