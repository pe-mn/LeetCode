# https://leetcode.com/problems/triangle/discuss/1169431/Short-and-Simple-Solutions-w-Explanation-or-4-Lines-of-Code-w-Comments

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for level in range(1, len(triangle)):
            for i in range(level+1):
                triangle[level][i] += min(triangle[level-1][min(i, level-1)], triangle[level-1][max(i-1,0)])
        return min(triangle[-1])        
            
              
        
# Wrong Answer        
# [[-1],[2,3],[1,-1,-3]] 
# Output 0
# Expected -1 (-1+3-3)
# ----------------------------
#         if len(triangle) == 1:
#             return triangle[0][0]
        
#         i = 0
#         sm = triangle[0][0]
#         for j, row in enumerate(triangle[1:]):
#             sm += min(row[i], row[i+1])
#             i = triangle[j+1].index(min(row[i], row[i+1]))            
#         return sm
            
# --------------------------------------------------------------                
        
#         if len(triangle) == 1:
#             return triangle[0][0]
        
#         i = 0
#         sums = []
#         sm = triangle[0][0]
#         for _ in range(len(triangle)):
#             for j, row in enumerate(triangle[1:]):
#                 # sm += min(row[i], row[i+1])
#                 # i = triangle[j+1].index(min(row[i], row[i+1]))
#             sums.append(sm)
#         return sm  