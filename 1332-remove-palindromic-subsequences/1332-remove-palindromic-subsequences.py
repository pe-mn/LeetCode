class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2 - (s == s[::-1]) - (s == "")

# Good to Know
# You need to know the difference between subarray and subsequence.
# Subarray need to be consecutive。
# Subsequence don't have to be consecutive.


# Intuition
# If it's empty sting, return 0;
# If it's palindrome, return 1;
# Otherwise, we need at least 2 operation.


# Explanation
# We can delete all characters 'a' in the 1st operation,
# and then all characters 'b' in the 2nd operation.
# So return 2 in this case


# Complexity
# Time O(N)
# Space O(N), also O(1) space checking palindrome is suuggested.

        
# Wrong Answer
# "ababb" Output 3 Expected 2
# -------------------------------

#         # Define a function to reverse string
#         def reverse_str(s):
#             return s[::-1]

#         #check if string is already palindrome
#         if s == s[::-1]:
#             return 1
        
#         # check if s is single character
#         if len(s) == 1:
#             return 1
    
#         counter = 0
#         remaining = s
#         for i in range(1, len(s)):
#             if remaining[i:] == reverse_str(remaining[i:]):
#                 remaining = remaining[:i]
#                 counter += 1
#                 # Condition to break the loop and return
#                 if len(remaining) == 1:
#                     return(counter+1)
             
#             elif s[:-i] == reverse_str(s[:-i]):
#                 remaining = remaining[-i:]
#                 counter += 1
#                 if len(remaining) == 1:
#                     return(counter+1) 
                
#         return counter