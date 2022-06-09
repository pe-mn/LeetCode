# 1-indexed not 0-indexed array

# A call to index results in a ValueError if the item's not present.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
# ---------------------------------------------------------------------- 
# Time Limit Exceeded
# [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,...], 2
# -----------------------------------------------------
        # for i, num in enumerate(numbers):
        #     if (target - num) in numbers[i+1:]:
        #         if i+1 == numbers.index(target-num)+1:
        #             return [i+1, [i for i, n in enumerate(numbers) if n == num][1]+1]
        #         else:
        #             return [i+1, numbers.index(target-num)+1]
        
# dictionary
# -------------
        # dic = {}
        # for i, num in enumerate(numbers):
        #     if target-num in dic:
        #         return [dic[target-num]+1, i+1]
        #     dic[num] = i

# binary search     
# -------------
        # for i in range(len(numbers)):
        #     l, r = i+1, len(numbers)-1
        #     tmp = target - numbers[i]
        #     while l <= r:
        #         mid = l + (r-l)//2
        #         if numbers[mid] == tmp:
        #             return [i+1, mid+1]
        #         elif numbers[mid] < tmp:
        #             l = mid+1
        #         else:
        #             r = mid-1

# ----------------------------------------------------------------------   
            
# two-pointer (Faster)
# --------------------
# l --> left, r --> right
        # l, r = 0, len(numbers)-1
        # while l < r:
        #     s = numbers[l] + numbers[r]
        #     if s == target:
        #         return [l+1, r+1]
        #     elif s < target:
        #         l += 1
        #     else:
        #         r -= 1
                

        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target: return (l + 1,  r + 1)
            if numbers[l] + numbers[r] > target: r -= 1
            else: l += 1
                
# Explanation:
# The array is sorted in increasing order.
# So, incresing left index gives bigger number and decresing right index gives smaller number.
# We start with left index as the 1st index and right index as the last index of the array.
# Calculate the sum of the two elements at the two indices.
# If it is greater than the target, that means we have to decrese the sum. So, we decrement the right index.
# If it is lesser than the target, that means we have to increse the sum. So, we inrement the left index.
# Continue this process untill the sum is equal to the target.
    
        
     
                
        