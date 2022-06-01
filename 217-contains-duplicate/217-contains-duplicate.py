class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
# we need only to compare the lengths 
# no need to compare the values 
# -----------------------------------------------------------------
        # return sorted(nums) != sorted(list(set(nums)))
# -----------------------------------------------------------------        
# Wrong Answer (as set changes the order)
# ---------------------------------------
        # return nums != list(set(nums))
    
# Time Limit Exceeded
# --------------------
        # for i, num in enumerate(nums):
        #     if num in nums[i+1:]:
        #         return True
        # return False
        