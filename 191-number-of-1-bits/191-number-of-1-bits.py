class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')
    
# --------------------------------------------------------------------------------------

        l = [a for a in bin(n) if a=='1']
        return len(l)        

# --------------------------------------------------------------------------------------
        
        # res = 0
        # while n != 0:
        #     if n % 2:
        #         res += 1
        #     n //= 2
        # return res