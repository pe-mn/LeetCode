# from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # sum = 0
        # for i, num in enumerate(nums):
        #     sum += num
        #     nums[i] = sum     
        # return nums
    
        # result = []
        # sum = 0
        # for i in range(len(nums)):
        #     sum += nums[i]
        #     result.append(sum)       
        # return result    
# ----------------------------------------------------- 
        return [sum(nums[:i]) for i in range(1, len(nums) + 1)]
# -----------------------------------------------------

# Here we also learning how can we use assignment inside comprehension \U0001f601 using :

        # s = 0; return [s:=s+v for v in nums]    
# -----------------------------------------------------
        # return accumulate(nums)
# -----------------------------------------------------
# That's so long... watch this:

# class Solution: runningSum = accumulate
