# https://leetcode.com/problems/longest-palindromic-substring/discuss/900639/Python-Solution-%3A-with-detailed-explanation-%3A-using-DP

# Dynamic Programming (DP) is an algorithmic technique for solving an optimization problem by breaking it down into simpler subproblems and utilizing the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems.

# Definition : the row and col in the dp table represent the slicing index on the string s (inclusive)
# example s = 'babad' -- > dp[2][3] = s[2:3] = ba

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
# Time Limit Exceeded
# ---------------------
#         longest_palindrom = ''
#         dp = [[0]*len(s) for _ in range(len(s))]
#         #filling out the diagonal by 1
#         for i in range(len(s)):
#             dp[i][i] = True
#             longest_palindrom = s[i]
			
#         # filling the dp table
#         for i in range(len(s)-1,-1,-1):
# 				# j starts from the i location : to only work on the upper side of the diagonal 
#             for j in range(i+1,len(s)):  
#                 if s[i] == s[j]:  #if the chars mathces
#                     # if len slicied sub_string is just one letter if the characters are equal, 
#                     # we can say they are palindomr dp[i][j] =True 
#                     #if the slicied sub_string is longer than 1, then 
#                     # we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
#                     if j-i ==1 or dp[i+1][j-1] is True:
#                         dp[i][j] = True
#                         # we also need to keep track of the maximum palindrom sequence 
#                         if len(longest_palindrom) < len(s[i:j+1]):
#                             longest_palindrom = s[i:j+1]
                
#         return longest_palindrom

# This solution is good, but slice takes O(k) times and spaces (where k is the length of the slice), so it is better to hold the indices of the longest palindrome in stead of palindrome itself.
# --------------------------------------------------------------------------------------
    
# Similar version but matrix in reverse, so somewhat easier to understand than OPs code.

        dp = [[False]*len(s) for _ in range(len(s)) ]
        for i in range(len(s)):
            dp[i][i]=True
            
        ans=s[0]
        for j in range(len(s)):
            for i in range(j):
                if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
                    dp[i][j]=True
                    if j-i+1>len(ans):
                        ans=s[i:j+1]
        return ans

# --------------------------------------------------------------------------------------
# Python easy to understand solution with comments (from middle to two ends).

#         res = ""
#         for i in range(len(s)):
#             # odd case, like "aba"
#             tmp = self.helper(s, i, i)
#             if len(tmp) > len(res):
#                 res = tmp
#             # even case, like "abba"
#             tmp = self.helper(s, i, i+1)
#             if len(tmp) > len(res):
#                 res = tmp
#         return res
    
# # get the longest palindrome, l, r are the middle indexes   
# # from inner to outer
#     def helper(self, s, l, r):
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             l -= 1; r += 1
#         return s[l+1:r]