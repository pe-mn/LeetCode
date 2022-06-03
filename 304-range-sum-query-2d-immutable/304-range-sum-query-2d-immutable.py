# https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/525902/Easy-understand-python-dynamic-programming-solution-O(m*n)

# This Explains the idea of the sums matrix
# https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/1716543/Simple-and-elegant-prefix-sum-matrix-with-explanation-faster-than-100

# class NumMatrix:
#     def __init__(self, matrix: List[List[int]]):
#         if matrix is None or not matrix:
#             return
#         # n --> rows, m --> columns
#         # i --> rows, j --> columns
#         n, m = len(matrix), len(matrix[0])
#         self.sums = [ [0 for j in range(m+1)] for i in range(n+1) ]
#         for i in range(1, n+1):
#             for j in range(1, m+1):
#                 self.sums[i][j] = matrix[i-1][j-1] + self.sums[i][j-1] + self.sums[i-1][j] - self.sums[i-1][j-1]
    

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
#         return self.sums[row2][col2] - self.sums[row2][col1-1] - self.sums[row1-1][col2] + self.sums[row1-1][col1-1]        

# To get the sum of area D, get the Whole Area sum of area A,B,C,D first. Then area D = Whole Area - area B - area C + area A because area B and area C both include A.

# -----------------------------------------------------------------------------------------

# class NumMatrix:
#     def __init__(self, matrix: List[List[int]]):
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if i==0 and j==0:
#                     continue
#                 elif i==0:
#                     matrix[i][j] += matrix[i][j-1]
#                 elif j==0:
#                     matrix[i][j] += matrix[i-1][j]
#                 else:
#                     matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
#         self.matrix = matrix
		
#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         a = b = c = d = 0
#         a = self.matrix[row2][col2]
#         if row1>0 and col1>0:
#             b = self.matrix[row1-1][col1-1]
#         if row1>0:
#             c = self.matrix[row1-1][col2]
#         if col1>0:
#             d = self.matrix[row2][col1-1]
#         return (a+b) - (c+d)

# -----------------------------------------------------------------------------------------

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):        
        if not matrix:
            # Reject empty matrix
            return
        
        # get height and width of matrix (also known as image)
        h, w = len(matrix), len(matrix[0])
        
        # build integral image by recurrence relationship    
        self.integral_image = [ [ 0 for _ in range(w) ] for _ in range(h) ]

        for y in range(h):
            summation = 0
            for x in range(w):
                summation += matrix[y][x]
                self.integral_image[y][x] = summation

                if y > 0:
                    self.integral_image[y][x] += self.integral_image[y-1][x]        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:        
        bottom_right    = self.integral_image[row2][col2]
        bottom_left     = self.integral_image[row2][col1-1] if col1 >= 1 else 0
        top_right       = self.integral_image[row1-1][col2] if row1 >= 1 else 0
        top_left        = self.integral_image[row1-1][col1-1] if col1 >= 1 and row1 >=1 else 0      
        return bottom_right - bottom_left - top_right + top_left
    
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


