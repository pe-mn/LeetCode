class Solution:
    def arraySign(self, nums: List[int]) -> int:
#         # Handle 0s
#         if 0 in nums:
#             return(0)
        
#         # Handle -ve cases
#         i = 0
#         for num in nums:
#             if num < 0:
#                 i+=1
        
#         return -1 if i%2 else 1

# --------------------------------------------------------------

# # [Python3] line sweep   
# -----------------------
        ans = 1
        for x in nums: 
            if x == 0: return 0 
            if x < 0: ans *= -1
        return ans   
    
# --------------------------------------------------------------
         
#         product = reduce(lambda x,y: x*y, nums)
#         return 0 if not product else 1 if product > 0 else -1

# --------------------------------------------------------------
        
         # return 0 if 0 in nums else -1 if sum(x < 0 for x in nums) % 2 else 1
        
# --------------------------------------------------------------
        
        # signs = False
        # for x in nums:
        #     if x == 0 : return 0
        #     signs = signs ^ (x < 0)
        # if signs : return -1
        # else: return 1