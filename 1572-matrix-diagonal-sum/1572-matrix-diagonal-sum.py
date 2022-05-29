class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # sum = 0
        # for i, row in enumerate(mat):
        #     for j, num in enumerate(row):
        #         if j==i or j+i==len(mat)-1:
        #             sum+=num                   
        # return sum
    
# ---------------------------------------------------------

	    # return sum(sum(r[j] for j in {i, len(r) - i - 1}) for i, r in enumerate(mat))

# ---------------------------------------------------------

        # return sum(v for i, r in enumerate(mat) for j, v in enumerate(r) if i+j == len(mat)-1 or i==j)

# ---------------------------------------------------------

        # n = len(mat)
        # return sum(mat[i][i] + mat[i][n - i - 1] for i in range(n)) - (mat[n // 2][n // 2] if n % 2 == 1 else 0)
    
# ---------------------------------------------------------

        # n = len(mat)
        # return sum(row[r] + row[n - 1 - r] for r, row in enumerate(mat)) - (0, mat[n // 2][n // 2])[n % 2]
    
# ---------------------------------------------------------

        # n = len(mat)
        # return sum(row[c] for r, row in enumerate(mat) for c in {r, n - 1 - r})
    
# ---------------------------------------------------------
 
        row,total = len(mat),0
        for i in range(row):
            total+=mat[i][i]+mat[i][row-i-1]
        return total-mat[row//2][row//2] if row%2!=0 else total
    
# ---------------------------------------------------------
    
        # n = len(mat)
        # row, primary_col, secondary_col = 0, 0, n-1
        # sum = 0
        # while row < n:
        #     sum += mat[row][primary_col]
        #     if secondary_col != primary_col:
        #         sum += mat[row][secondary_col]
        #     row += 1
        #     primary_col += 1
        #     secondary_col -= 1
        # return sum

# ---------------------------------------------------------

# I turned the entries I visited to zero to prevent double summation.
        # n = len(mat)
        # s = 0
        # for i in range(n):
        #     s+= mat[i][i]
        #     mat[i][i] = 0
        #     s+= mat[-i-1][i]
        # return s

# ---------------------------------------------------------
    
#         n = len(mat)
#         ans = 0
        
#         # Sum over each corner
#         for i in range(n // 2):
#             ans += mat[i][i] + mat[i][~i] + mat[~i][i] + mat[~i][~i]
            
#         # If the length is odd, add the middle element
#         if (n % 2) == 1:
#             i = n // 2 
#             ans += mat[i][i]
#         return ans
    
# ---------------------------------------------------------
    
#         n = len(mat)     
#         mid = n // 2        
#         summation = 0
        
#         for i in range(n):            
#             # primary diagonal
#             summation += mat[i][i]            
#             # secondary diagonal
#             summation += mat[n-1-i][i]
                        
#         if n % 2 == 1:
#             # remove center element (repeated) on odd side-length case
#             summation -= mat[mid][mid]
                        
#         return summation
    
    
