class Solution:
    def isPossible(self, target: List[int]) -> bool:
# Backtrack, OJ is wrong
        total = sum(target)
        target = [-a for a in target]
        heapq.heapify(target)
        while True:
            a = -heapq.heappop(target)
            total -= a
            if a == 1 or total == 1: return True
            if a < total or total == 0 or a % total == 0:
                return False
            a %= total
            total += a
            heapq.heappush(target, -a)

# Foreword
# By the way, I planed to update this post ealier.
# I didn't do that, not because of lazy.
# I understand that you have expectation on me or the top voted post,
# but I also have expectation of LC.
# But lc doesn't do its work at all (in my mind),
# Someone would rather believe the misleading "Accepted",
# Honestly, I cannot do better in this case like that.


# Weak test case
# Problem is good, tests cases are trash.
# Missing test cases:
# [1]
# [2]
# [1, 2]
# [1,1,2]
# [1, 1000000000]
# [5, 50]


# Wrong OJ
# Yes, OJ needs a solution to run the test cases.
# But the OJ for this problem fail the case [1, 1000000000], which expects true


# Explanation
# The total sum always bigger than all elements.
# We can decompose the biggest number.
# Each round we get the current maximum value,
# delete it by the sum of other elements.

# Time O(N) to build up the priority queue.
# Time O(logMaxAlogN)) for the reducing value part.
# We have O(maxA) loops, which is similar to gcd
# Space O(N)

# % operation is totally much more important than using heap.
# If brute force solution is accepted,
# then the solutions without % are right and good.

# But the truth is that, solution without % should be TLE.
# So I afraid that, without % is wrong to me.




        
#------------------------------------------------------        
# Wrong Answer
# Input: [8,5]
# Output: False
# Expected: True
#------------------------------------------------------
# You may repeat this procedure as many times as needed.
        # if len(target) not in target:
        #     return False
#------------------------------------------------------
#         arr = [1 for _ in range(len(target))]
#         res = True
#         for i in range(len(target)):
#             if sum(arr) in target:
#                 arr[target.index(sum(arr))] = sum(arr)              
#             else: 
#                 res = False
            
#         print(arr)
#         return res
# ------------------------------------------------------------------  
# Wrong Answer
# Input: [8,5]
# Output: False
# Expected: True
#------------------------------------------------------
# You may repeat this procedure as many times as needed.
        # if len(target) not in target:
        #     return False
#------------------------------------------------------
#         target.sort()
#         if len(target) > target[-1]:
#             return False
        
#         arr = [1 for _ in range(len(target))]
#         for i in range(len(target)):
#             if sum(arr) in target:
#                 arr[target.index(sum(arr))] = sum(arr)              
            
#         print(arr)
#         return arr == target
            
        