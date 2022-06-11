# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/1016199/Python-O(n)-solution-using-cumulative-sums

# We can reformulate this problem: we need to choose several values from the beginning and several values from end, such that sum of this numbers is equal to x. It is equivalent to finding some contiguous subarray, such that it has sum of elements equal to sum(nums) - x, which has the biggest length. In this way problem becomes quite classical and I prefer to solve it using cumulative sums.

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int: 
#         # append [0] to the beginning to modify cumsums indices
#         cumsum = [0] + list(accumulate(nums))
#         dic = {c:i for i,c in enumerate(cumsum)}
#         goal = cumsum[-1] - x
#         ans = -float("inf")

#         # This means tha x > sum(nums)
#         if goal < 0: return -1

#         for num in dic:
#             if num + goal in dic:
#                 ans = max(ans, dic[num + goal] - dic[num])

#         return len(nums) - ans if ans != -float("inf") else -1     
    
# ------------------------------------------------------------------------------
# Using sliding window to find the longest subarry that sums to sum(nums) - x
# ------------------------------------------------------------------------------
        target, size, win_sum, lo, n = sum(nums) - x, -1, 0, -1, len(nums)
        for hi, num in enumerate(nums):
            win_sum += num
            while lo + 1< n and win_sum > target:
                lo += 1
                win_sum -= nums[lo]
            if win_sum == target:
                size = max(size, hi - lo)
        return -1 if size < 0 else n - size
        
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
        