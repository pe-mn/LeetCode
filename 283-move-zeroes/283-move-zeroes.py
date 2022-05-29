# https://stackoverflow.com/questions/4081217/how-to-modify-list-entries-during-for-loop
# You can’t use for-in loop to modify a list
# https://www.quora.com/Why-can%E2%80%99t-you-modify-lists-through-for-in-loops-in-Python

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
# Two pointers technique (Python, O(n) time / O(1) space)
# -------------------------------------------------------     
#         slow = 0
#         for fast in range(len(nums)):
#             if nums[fast] != 0:
#                 nums[slow], nums[fast] = nums[fast], nums[slow]

#             # wait while we find a non-zero element to
#             # swap with you
#             if nums[slow] != 0:
#                 slow += 1      

# Algorithm complexity:
# Time complexity: O(n). Our fast pointer does not visit the same spot twice.
# Space complexity: O(1). All operations are made in-place
        
# maybe we don't need nums[slow] == 0.
# slow will jump to next value by if nums[slow] != 0 after swap.        
                       
# -------------------------------------------------------------         
        
# Wrong Answer, Since we modify nums while using it in the loop
# ------------------------------------------------------------- 
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         # del nums[i]
        #         nums.pop(i)
        #         nums.append(0)

# Correct Answer 
#----------------
# its because if we start traversing the list from the last index, deleting/popping out the zeros wont affect the indexes of the elements in the list that we havent checked yet. Hope that makes some sense.
# ------------------------------------------------------------- 
        # for i in range(len(nums))[::-1]:
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
# ------------------------------------------------                          
        
# Wrong Answer, Since we modify nums while using it in the loop
# -------------------------------------------------------------      
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         # del nums[i]
        #         nums.pop(i)
        #         nums.append(0)
                
# Wrong Answer, Since we need to modify nums in place
# ---------------------------------------------------
        # n = nums.count(0)
        # no_zero = [i for i in nums if i!= 0]
        # zeros = [0] * n    
        # nums = no_zero + zeros

# Correct Answer        
# ---------------                   
        # count=nums.count(0)
        # nums[:]=[i for i in nums if i != 0]
        # nums+=[0]*count        
        
# ------------------------------------------------        
        # n = nums.count(0)
        # while(0 in nums):
        #     nums.remove(0)
        # nums.extend([0]*n)  
# ------------------------------------------------        
        for j in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)    
# ------------------------------------------------                    

        # zero = 0  # records the position of "0"
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[i], nums[zero] = nums[zero], nums[i]
        #         zero += 1

        
                