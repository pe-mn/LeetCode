class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         start = maxLength = 0
#         usedChar = {}
        
#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i-start+1)

#             usedChar[s[i]] = i
#         return maxLength
    
# ---------------------------------------------------------------------------    
# If you use 'enumerate', code will be more readable.
    
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i-start+1)
            
            used[c] = i  
        return max_length    
        
# ---------------------------------------------------------------------------    
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation     
# Sliding window
# ---------------
# We use a dictionary to store the character as the key, the last appear index has been seen so far as value.
# seen[charactor] = index
# move the pointer when you met a repeated character in your window.

#         seen = {}
#         l = 0
#         output = 0
#         for r in range(len(s)):
#         # If s[r] not in seen, we can keep increasing the window size by moving right pointer
#             if s[r] not in seen:
#                 output = max(output,r-l+1)
# # There are two cases if s[r] in seen:
# # case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
# # case2: s[r] is not inside the current window, we can keep increase the window
#             else:
#                 if seen[s[r]] < l:
#                     output = max(output,r-l+1)
#                 else:
#                     l = seen[s[r]] + 1
#             seen[s[r]] = r
#         return output
    
# ---------------------------------------------------------------------------    
        
# Wrong Answer 
# Python dictionaries don't support duplicate keys.
# So, strt value in wrong
# --------------------------------------------------
        # if len(set(s))==1: return 1
        # seen = set()
        # sub_dict = {}
        # strt = 0
        # for i, char in enumerate(s):
        #     if char not in seen:
        #         seen.add(char)
        #     else:  
        #         seen = set()
        #         try: strt = sum(sub_dict.values())
        #         except: pass
        #         print(strt)
        #         sub_dict[s[strt:i]] = len(s[strt:i])  
        #         print(sub_dict)
        # return max(sub_dict.values())        
        
        
# Wrong Answer 
# Input "bbbbb"
# Output 2
# Expected 1
# -------------
        # seen = set()
        # sub_dict = {}
        # strt = 0
        # for i, char in enumerate(s):
        #     if char not in seen:
        #         seen.add(char)
        #         strt = i
        #     else:     
        #         sub_dict[s[strt+1:i-1]] = len(s[strt+1:i-1])             
        # return max(sub_dict.values())
    

# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# max(sub_dict, key=sub_dict.get)
# max(sub_dict)

# https://stackoverflow.com/questions/10664856/make-a-dictionary-with-duplicate-keys-in-python


                                
        