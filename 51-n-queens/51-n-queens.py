# https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            """`valid_configs` contains configurations of n queens that satisfy
            threat constraints.

            Each element in `queens` represents the position of a queen.
            Its row is indicated by the element *index* and its column is
            indicated by the element *value*. Given this, duplicate values
            in `queens` would mean two rows had a queen in the same column,
            which isn't allowed.
            
            yx_diffs and yx_sums both represent diagonals that are threatened
            by a queen in `queens`. As shown below, diagonals can be represented
            with a single integer calculated from the difference or sum of a
            position's row and columns indices. Differences (row - col) are
            left->right diagonals and sums are right->left diagonals.
            
            yx_diffs (row_idx - col_idx):
            3 |  3  2  1  0
            2 |  2  1  0 -1
            1 |  1  0 -1 -2
            0 |  0 -1 -2 -3
            r  ------------
              c  0  1  2  3

            yx_sums (row_idx + col_idx):
            3 |  3  4  5  6
            2 |  2  3  4  5
            1 |  1  2  3  4
            0 |  0  1  2  3
            r  ------------
              c  0  1  2  3
            """        
            p = len(queens)  # p is the index of row
            if p==n:
                result.append(queens)
                return None
            for q in range(n):  # q is the index of col 
                # queens stores those used cols, for example, [0,2,4,1] means these cols have been used
                # xy_dif is the diagonal 1
                # xy_sum is the diagonal 2
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
    
# Use the DFS helper function to find solutions recursively. A solution will be found when the length of queens is equal to n ( queens is a list of the indices of the queens).

# In this problem, whenever a location (x, y) is occupied, any other locations (p, q ) where p + q == x + y or p - q == x - y would be invalid. We can use this information to keep track of the indicators (xy_dif and xy_sum ) of the invalid positions and then call DFS recursively with valid positions only.

# At the end, we convert the result (a list of lists; each sublist is the indices of the queens) into the desire format.


# I feel like no one ever explains the logic for checking against diagonals in lamen terms. Basically since all slopes are either (-1) or (1) going up or down (we only care about 45/135 degree slopes, we are bascially taking a coord and solving for the y intercept in the slop intercept for y = mx + b. This always transforms into two forms in our case since we have two slopes. EITHER: y = (-1)x + b -> y = -x + b -> y + x = b OR y = 1x + b -> y = x + b -> y - x = b. So either on the up or down slope you solve for where a point on this line would intercept the y axis. Something to note is even though a slope looks like its going downward in a visual image of a 2d grid, you need to check if the indices are actually increasing, in programming we usually draw our grids backwards where the y axis value increases as it grows downward. This could cause you to assume the wrong slope. Anyway, you plug the slope and coord for your point in y = mx + b the result will be b = (some value). That is the y intercept and it will be consistent across any point on the same line so you can tell in constant time via a lookup table if any other queens have been placed on this line. I havent done geometry in literally over 10 years, but thats what I understand about that step... Correct me if that was wrong or even too much.
        