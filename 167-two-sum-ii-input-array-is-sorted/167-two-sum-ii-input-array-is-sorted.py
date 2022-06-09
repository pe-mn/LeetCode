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
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
            
            
# two-pointer
# -------------
        # l, r = 0, len(numbers)-1
        # while l < r:
        #     s = numbers[l] + numbers[r]
        #     if s == target:
        #         return [l+1, r+1]
        #     elif s < target:
        #         l += 1
        #     else:
        #         r -= 1
    
        
# binary search     
# -------------
        # for i in xrange(len(numbers)):
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
        # for i, num in enumerate(numbers):
        #     if num < target:
                
        