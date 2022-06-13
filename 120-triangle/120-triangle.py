# https://leetcode.com/problems/triangle/discuss/1169431/Short-and-Simple-Solutions-w-Explanation-or-4-Lines-of-Code-w-Comments

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
# ✔️ Solution - I (In-Place Bottom-Up Dynamic Programming)
        # for level in range(1, len(triangle)):
        #     for i in range(level+1):
        #         triangle[level][i] += min(triangle[level-1][min(i, level-1)], triangle[level-1][max(i-1,0)])
        # return min(triangle[-1])  

# For anyone like me struggling to understand min(triangle[level-1][min(i, level-1)], triangle[level-1][max(i-1,0)])
        m = len(triangle)
        
        # Loop every level in the triangle
        for level in range(1, m):
            # Every level has n elements (n = level). Loop through them
            for i in range(level+1):
                # If you are at the first index at the current level, 
                # you can only add the first element of the previous level
                if i == 0:
                    triangle[level][i] += triangle[level-1][0]
                    
                # If you are at the last index at the current level, 
                # you can only add the last element of the previous level
                elif i == level:
                    triangle[level][i] += triangle[level-1][i-1]
                    
                # For the middle elements
                # You can either add the previous level same index or previous level index - 1
                # Whichever is smaller
                else:
                    triangle[level][i] += min(triangle[level-1][i], triangle[level-1][i-1])
                        
        return min(triangle[-1])


# ✔️ Solution - II (In-Place Top-Down Dynamic Programming)
        # for level in range(len(triangle)-2,-1,-1):
        #     for i in range(level+1):
        #         triangle[level][i] += min(triangle[level+1][i], triangle[level+1][i+1])
        # return triangle[0][0]
        
# Solution - III (Bottom-Up Dynamic Programming w/ Auxillary Space)
	    # n = len(triangle)
	    # cur_row, prev_row = [0]*n, [0]*n
	    # prev_row[0] = triangle[0][0]  
	    # for level in range(1, n):
	    # for i in range(level+1):
	    # cur_row[i] = triangle[level][i] + min(prev_row[min(i, level-1)], prev_row[max(i-1,0)])
	    # cur_row, prev_row = prev_row, cur_row
	    # return min(prev_row)

# Solution - IV (Top-Down Dynamic Programming w/ Auxillary Space)
        # n = len(triangle)
        # cur_row, next_row = [0]*n, triangle[n-1]        
        # for level in range(n-2,-1,-1):
        #     for i in range(level+1):
        #         cur_row[i] = triangle[level][i] + min(next_row[i], next_row[i+1])
        #     cur_row, next_row = next_row, cur_row
        # return next_row[0]

     
    
# ----------------------------        
# Wrong Answer        
# [[-1],[2,3],[1,-1,-3]] 
# Output 0
# Expected -1 (-1+3-3)
# ----------------------------
# We can easily see that directly just choosing the minimum value in the next row(amongst triangle[nextRow][i] and triangle[nextRow][i+1]) won't fetch us the optimal final result since it maybe the case that the latter values of previous chosen path turn out to be huge.
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