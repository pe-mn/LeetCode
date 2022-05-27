class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
#         # Handle Edge Cases
#         if len(arr) < 2:
#             return True
        
#         # arr = sorted(arr)
#         arr.sort()
#         diff = arr[1] - arr [0]
                        
#         for i in range(1, len(arr)-1):
#             if arr[i+1] - arr [i] != diff:
#                 return False
                
#         return True

# --------------------------------------------------------------------

# # Clean Python 3, O(N)
# ----------------------               
        # m = min(arr)
        # gap = (max(arr) - m) / (len(arr) - 1)
        # if gap == 0: return True
        # s = set(num - m for num in arr)
        # return len(s) == len(arr) and all(diff % gap == 0 for diff in s)                    
# --------------------------------------------------------------------
            
        # arr.sort()
        # return len(set(arr[i-1] - arr[i] for i in range(1, len(arr)))) == 1        
    
# --------------------------------------------------------------------

        return arr.sort() or all([(j-i) == arr[1] - arr[0] for i, j in zip(arr, arr[1:])])