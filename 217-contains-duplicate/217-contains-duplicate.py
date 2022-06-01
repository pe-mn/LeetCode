class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
    
        # return len(nums) > len(set(nums))
    
# we need only to compare the lengths 
# no need to compare the values 

# However, it actually did more work than others' common code. Their process would mostly did less iterations, thus ending sooner than yours. You don't necessarily form up the whole set.
# -----------------------------------------------------------------
        # return sorted(nums) != sorted(list(set(nums)))
# ----------------------------------------------------------------- 
# https://leetcode.com/problems/contains-duplicate/discuss/1521790/4-solutions-in-Python

# use sort()
# Time Complexity: O(n Log n)
# Space Complexity: O(1)

        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False      
        
# use hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)        
 
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] not in hashTable:
                hashTable[nums[i]] = 1
            else:
                hashTable[nums[i]] += 1
        
        for i in range(len(nums)):
            if hashTable[nums[i]] >= 2:
                return True
        return False
    
    
        # hashTable = {}
        # for i in range(len(nums)):
        #     if nums[i] not in hashTable:
        #         hashTable[nums[i]] = 1
        #     else:
        #         return True
        # return False
# ----------------------------------------------------------------- 

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
        
# Brute force
# Time Complexity: O(n^2) [It gets Time Limit Exceeded when n ≥10^5]
# Space Complexity: O(1)

# Time Limit Exceeded
# --------------------
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        