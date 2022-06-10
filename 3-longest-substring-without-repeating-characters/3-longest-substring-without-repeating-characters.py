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
    
#         used = {}
#         max_length = start = 0
#         for i, c in enumerate(s):
#             if c in used and start <= used[c]:
#                 start = used[c] + 1
#             else:
#                 max_length = max(max_length, i-start+1)
            
#             used[c] = i  
#         return max_length    
        
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
        # if s=="": return 0
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
        
# ---------------------------------------------------------------------------    
        
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
        
# ---------------------------------------------------------------------------   
# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/347818/Python3%3A-sliding-window-O(N)-with-explanation     
# Sliding window
# ---------------
# We use a dictionary to store the character as the key, the last appear index has been seen so far as value.
# seen[charactor] = index
# move the pointer when you met a repeated character in your window.

        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            # when char already in dictionary
            if ch in dic:
                # check length from start of string to index
                res = max(res, i-start)
                # update start of string index to the next index
                start = max(start, dic[ch]+1)
            # add/update char to/of dictionary 
            dic[ch] = i
        # answer is either in the begining/middle OR some mid to the end of string
        return max(res, len(s)-start) 
        # as the last substring will not enter the loop to update res

        
# ---------------------------------------------------------------------------    
# {'p': 0}
# {'p': 0, 'w': 1}
# enter loop
# {'p': 0, 'w': 2}
# {'p': 0, 'w': 2, 'k': 3}
# {'p': 0, 'w': 2, 'k': 3, 'e': 4}
# enter loop
# {'p': 0, 'w': 5, 'k': 3, 'e': 4}   

        # d, res, start = {}, 0, 0
        # for i, ch in enumerate(s):
        #     if ch in d: start = max(start, d[ch]+1)
        #     res = max(res, i-start+1)                
        #     d[ch] = i
        # return res 
# ---------------------------------------------------------------------------    

# Wrong Answer 
# Input "abba"
# Output 3
# Expected 2
# -------------
        # dic, res, start, = {}, 0, 0
        # for i, ch in enumerate(s):
        #     # when char already in dictionary
        #     if ch in dic:
        #         # check length from start of string to index
        #         res = max(res, i-start)
        #         # update start of string index to the next index
        #         start = dic[ch]+1
        #     # add/update char to/of dictionary 
        #     dic[ch] = i
        # # answer is either in the begining/middle OR some mid to the end of string
        # return max(res, len(s)-start) 
        # # as the last substring will not enter the loop to update res
        
# Basically start can't move left. It can only move right. So either move it right or leave it unchanged. You only move it right when start is less than the current repetition. If start has somehow moved ahead then there's no need to move it left. For example in abba. When the second a is encountered, start has moved ahead from first a. But the map still remembers that as the last seen a. Now just to eleimitate the left a if we move start by just 1 then it will land on first b. start moved backwards. Before it was on second b and now it is on first b. Just don't update it in this case. Just update the repeated character position in the map and now back to normal, start has become less than the next repeating a, so now start can move, if it sees another a.
   

# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# max(sub_dict, key=sub_dict.get)
# max(sub_dict)

# https://stackoverflow.com/questions/10664856/make-a-dictionary-with-duplicate-keys-in-python


                                
        