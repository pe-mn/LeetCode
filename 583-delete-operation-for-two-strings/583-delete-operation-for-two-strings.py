# https://leetcode.com/problems/delete-operation-for-two-strings/discuss/1195726/C%2B%2BPythonJava-Short-and-Easy-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP

# https://leetcode.com/problems/delete-operation-for-two-strings/discuss/103246/Python-DP-solution

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
# The same as finding longest common sub sequence:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (word1[i] == word2[j]))
        return m + n - 2 * dp[m][n]        