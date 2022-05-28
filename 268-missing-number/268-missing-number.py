class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
# **Slow:**
# check for each number in range len(nums)+1, since we have one missing number in that range

        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
            
# -------------------------------------------------------

# **Fast:**
# We can spot the missing number as the difference in sums between the numbers and the range (with no missing)

#         return sum(range(len(nums)+1)) - sum(nums)
    
# -------------------------------------------------------

# **Faster:**
# sum(range(len(nums)+1)) can be replaced by this formula (n * (n+1)) // 2 
# **Expalanation:**  For instance, if we want to sum all numbers from 1 to 100:
# 1+100 = 101, 2+99 = 101, 3+88 = 101, ..., 51+50 = 101
# so the result would be: ```100*(100+1)/2``` i.e. ``` (n*(n+1))//2 

        n = len(nums)
        return ((n * (n+1)) // 2) - sum(nums) 
    