class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # return sorted(s) == sorted(t)
# ---------------------------------------------------------------------        
        # return all([s.count(c)==t.count(c) for c in string.ascii_lowercase])
# ---------------------------------------------------------------------        
        # return collections.Counter(s) == collections.Counter(t)
# ---------------------------------------------------------------------
# Using defaultdict beats 97%
# ---------------------------
        # if len(s) != len(t):
        #     return False 
        # count = collections.defaultdict(int)
        # for c in s:
        #     count[c] += 1
        # for c in t:
        #     count[c] -= 1
        #     if count[c] < 0:
        #         return False
        # return True
# ---------------------------------------------------------------------
    
#         dic1, dic2 = {}, {}
#         for item in s:
#             dic1[item] = dic1.get(item, 0) + 1
#         for item in t:
#             dic2[item] = dic2.get(item, 0) + 1
#         return dic1 == dic2
    
#         dic1, dic2 = [0]*26, [0]*26
#         for item in s:
#             dic1[ord(item)-ord('a')] += 1
#         for item in t:
#             dic2[ord(item)-ord('a')] += 1
#         return dic1 == dic2

# instead of writing two for loops for s and t each, we can write in a single loop.        
        # if len(s) != len(t) : 
        #     return False
        # dict1 = [0]*26 
        # dict2 = [0] * 26
        # for i in range(len(s)) : 
        #     dict1[ord(s[i])-ord('a')] += 1
        #     dict2[ord(t[i]) - ord('a')] += 1
        # return dict1 == dict2 
        
# instead of creating a second dictionary, we can try to "delete" from the first dictionary to save space.
        if len(s) == len(t):
            chars = defaultdict(int)
            for l in s:
                chars[l] += 1
            
            for l in t:
                chars[l] -= 1
            
            return all(v == 0 for v in chars.values())
        return False
# ---------------------------------------------------------------------

#         dic = {}
#         for i in s:
#             if i not in dic:
#                 dic[i] = 1
#             else:
#                 dic[i] += 1
        
#         for j in t:
#             if j not in dic:
#                 return False
#             else:
#                 dic[j] -= 1
        
#         for val in dic.values():
#             if val != 0:
#                 return False       
#         return True
        
# ---------------------------------------------------------------------
    
        # d = dict()
        # for i in s:
        #     d[i] = d.get(i, 0) + 1        
        # for j in t:
        #     if j not in d:
        #         return False
        #     else:
        #         d[j] -= 1
        # return all(x==0 for x in d.values())