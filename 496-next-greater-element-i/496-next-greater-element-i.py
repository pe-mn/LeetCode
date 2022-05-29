# Thank you very much. I got asked this question in Amazon and one other company. 

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 contains the elements to check in nums2
        d = {}     
        for i,num1 in enumerate(nums2):
            for num2 in nums2[i+1:]:
                 if num2 > num1:
                        d[num1] = num2
                        break
        return [d.get(num1,-1) for num1 in nums1]
    
# --------------------------------------------------------------

#         d, st, ans = {}, [], []
        
#         for x in nums2:
#             while len(st) and st[-1] < x:
#                 d[st.pop()] = x
#             st.append(x)

#         # for x in nums1:
#         #     ans.append(d.get(x, -1))
#         # return ans  
    
#         return [d.get(x, -1) for x in findNums]        
    
    
# TypeError: 'builtin_function_or_method' object is not subscriptable res.append[1]
# Looks like you typed brackets instead of parenthesis by mistake.      