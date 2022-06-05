# https://leetcode.com/problems/n-queens-ii/discuss/1238198/Python-Super-short-backtracking-explained

class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(board, i, c1, c2, c3):
            if i == n: self.ans += 1
            
            for j in range(n):
                if c1 & 1<<j or c2 & 1<<i-j+n or c3 & 1<<i+j: continue
                dfs(board + [j], i + 1, c1 ^ 1<<j, c2 ^ 1<<i-j+n, c3 ^ 1<<i+j)
        
        self.ans = 0
        dfs([], 0, 0, 0, 0)
        return self.ans    
    
# This problem is similar to problem 46 and 51, basically we need to go over all n! permutations and then check if it is correct and write function to draw this solution. Let us use dfs(board, c1, c2, c3) function here, where:

# board are positions of queen for the first, second and so on lines. Length of board is how many queens we already used.
# c1 is bit mask for columns, c2 and c3 for diagonals. Note, that we use i-j+n for one of the diagonals to avoid negative numbers. Each time we try to take all possible positions and then check if we can put queen on this position.
# Complexity -->Time and space complexity is O(n!).