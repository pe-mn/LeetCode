# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/1019513/Python-QuickSelect-average-O(n)-explained

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
# QuickSelect
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0] 
        
# # ------------------------------------------------------------      

# # O(nk) time, bubble sort idea, TLE
#         for i in range(k):
#             for j in range(len(nums)-i-1):
#                 if nums[j] > nums[j+1]:
#                     # exchange elements, time consuming
#                     nums[j], nums[j+1] = nums[j+1], nums[j]
#         return nums[len(nums)-k]
    
# # O(nk) time, selection sort idea
#         for i in xrange(len(nums), len(nums)-k, -1):
#             tmp = 0
#             for j in xrange(i):
#                 if nums[j] > nums[tmp]:
#                     tmp = j
#             nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
#         return nums[len(nums)-k]
    
# # O(k+(n-k)lgk) time, min-heap
#         heap = []
#         for num in nums:
#             heapq.heappush(heap, num)
#         for _ in xrange(len(nums)-k):
#             heapq.heappop(heap)
#         return heapq.heappop(heap)
    
#         heap = nums[:k]
#         heapify(heap)
#         for n in nums[k:]:
#             heappushpop(heap, n)
#         return heap[0]

# # O(k+(n-k)lgk) time, min-heap        
#         return heapq.nlargest(k, nums)[-1]

# # ------------------------------------------------------------      
    
# # O(n) time, quick selection
# def findKthLargest(self, nums, k):
#     # convert the kth largest to smallest
#     return self.findKthSmallest(nums, len(nums)+1-k)
    
# def findKthSmallest(self, nums, k):
#     if nums:
#         pos = self.partition(nums, 0, len(nums)-1)
#         if k > pos+1:
#             return self.findKthSmallest(nums[pos+1:], k-pos-1)
#         elif k < pos+1:
#             return self.findKthSmallest(nums[:pos], k)
#         else:
#             return nums[pos]
        
# # choose the right-most element as pivot   
# def partition(self, nums, l, r):
#     low = l
#     while l < r:
#         if nums[l] < nums[r]:
#             nums[l], nums[low] = nums[low], nums[l]
#             low += 1
#         l += 1
#     nums[low], nums[r] = nums[r], nums[low]
#     return low               
        
# ------------------------------------------------------------      
        # nums.sort(reverse=True)
        # return nums[k-1]
# ------------------------------------------------------------  
# O(nlgn) time
        # return sorted(nums, reverse=True)[k-1]
# ------------------------------------------------------------      
        # return sorted(nums)[-k]
# ------------------------------------------------------------ 