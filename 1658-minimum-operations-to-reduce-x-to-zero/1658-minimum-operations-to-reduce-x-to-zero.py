class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:   
        cumsum = [0] + list(accumulate(nums))
        dic = {c:i for i,c in enumerate(cumsum)}
        goal = cumsum[-1] - x
        ans = -float("inf")

        if goal < 0: return -1

        for num in dic:
            if num + goal in dic:
                ans = max(ans, dic[num + goal] - dic[num])

        return len(nums) - ans if ans != -float("inf") else -1              
        
# ---------------------------------        
# Wrong Answer (Corrected)
# Input: [1,1], 3
# output: 3
# Expected -1
# As i, j should stop at some point
# -----------------------------------
# This is not the right approach, as subtracting the maximum
# Could lead to a remaining that cannot reach 0 by minimums

#         remaining = x; i = 0; j = len(nums)-1; counter = 0
#         while remaining > 0 and i<=j: 
#             if max(nums[i], nums[j]) <= remaining:
#                 remaining = remaining - max(nums[i], nums[j])
#                 counter += 1
#                 print(remaining)
#                 if nums[i] > nums[j]:
#                     i += 1; 
#                 else: 
#                     j-= 1   
                    
#             else:
#                 remaining = remaining - min(nums[i], nums[j])
#                 counter += 1
#                 print(remaining)
#                 if nums[i] < nums[j]:
#                     i += 1; 
#                 else: 
#                     j-= 1                    
#         return counter if remaining == 0 else -1   
        
# --------------------------------------------------------------------

        # remaining = x; i = 0; j = len(nums)-1
        # while remaining >= 0: 
        #     remaining = remaining - max(nums[i], nums[j])
        #     i += 1
        #     j-= 1           
        # return i-1
        