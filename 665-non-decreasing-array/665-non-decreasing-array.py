# https://leetcode.com/problems/non-decreasing-array/discuss/1190763/JS-Python-Java-C%2B%2B-or-Simple-Solution-w-Visual-Explanation

# https://leetcode.com/problems/non-decreasing-array/discuss/106816/Python-Extremely-Easy-to-Understand

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:          
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)
# ---------------------------------------------------------------------------------------
    
        # err = 0
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         if err or (i > 1 and i < len(nums) - 1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
        #             return False
        #         err = 1
        # return True
    
# ---------------------------------------------------------------------------------------
    
#         p, n = -1, len(nums)
#         for i in range(n - 1):
#             if nums[i] > nums[i+1]:
#                 if p != -1: return False
#                 p = i

#         return p in [-1, 0, n-2] or nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2]  
    
# https://leetcode.com/problems/non-decreasing-array/discuss/1190833/Python-O(n)-solution-explained
        
# What we need to check is the following: first, that we have only one pair of adjacent elements, such that first is more then the next one. If we found two such elements, we return False. If there is not such elements, we return True. Also we return True if this element is the first or the last. Finally, we return True if we can remove this element and have A[p-1] <= A[p+1] or remove next element and have A[p] <= A[p+2].

# Complexity
# Time complexity is O(n), space is O(1).        
        
# ---------------------------------------------------------------------------------------

        # n = len(nums)
        # to_modify = 0  # elements to modify 
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[j] < nums[i]:
        #             to_modify += 1
        #             nums.remove(nums[i])
        #             n -= 1
        #         # This line is used to breack the loop once the counts of 
        #         # elements that needs to be modified exceeds 1 
        #         if to_modify > 1: return False
        # return True  
        
 # ---------------------------------------------------------------------------------------
       
# Remove one element which is out of ascending order
# Then check if the list is sorted return True
# else return False

# Runtime Error
# But this could take a lot of coputational power to sort large arrays
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)-1):
        #         if nums[j] < nums[i]:
        #             nums.remove(nums[i])
        #             return nums == sorted(nums)
            
        
# ---------------------------------------------------------------------------------------
        
# Wrong Answer
# [5,7,1,8]
        # to_modify = 0  # elements to modify 
        # for i in range(len(nums)-1):
        #     if any(nums[j] < nums[i] for j in range(i+1, len(nums))):
        #         to_modify += 1
        #         # This line is used to breack the loop once the counts of 
        #         # elements that needs to be modified exceeds 1 
        #         if to_modify > 1: return False
        # return True
        
# ---------------------------------------------------------------------------------------
        
# Wrong Answer
# [3,4,2,3]
        # return sum([nums[i] > nums[i+1] for i in range(len(nums)-1)]) <= 1
        