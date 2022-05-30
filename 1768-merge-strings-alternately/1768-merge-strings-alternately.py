class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
#         w = ''
#         for c1, c2 in zip(word1, word2):
#             w += c1+c2  
        
#         n1, n2 = len(word1), len(word2)
#         if n1 == n2:
#             return w 
#         elif n1 > n2:
#             return w + word1[n2: n2+(n1-n2)]
#         else:
#             return w + word2[n1: n1+(n2-n1)]
        
# --------------------------------------------------------------------------
        # return ''.join(c1 + c2 for c1, c2 in zip_longest(word1, word2, fillvalue=''))
# --------------------------------------------------------------------------
        # return ''.join(chain(*zip_longest(word1, word2, fillvalue='')))
    
# Since strings are immutable in python, we will be allocating O(max(m, n)) extra space (not the result) for the intermediate concatenations a + b.
# We could avoid this by using chain on the zip:

# This will pass the unmodified values straight to str.join, which will result in only allocating one new string, the result. The space requirements of join will still take up the same space, so we don't win in terms of total space complexity. We just avoid a bunch of string copying.
# --------------------------------------------------------------------------
        res=''
        
        for i in range(min(len(word1),len(word2))):
            res += word1[i] + word2[i]
            
        return res + word1[i+1:] + word2[i+1:]
# --------------------------------------------------------------------------

            