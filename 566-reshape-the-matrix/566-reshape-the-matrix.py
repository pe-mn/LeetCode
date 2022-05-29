import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
# 		# Creat a flat matrix
#         flat_mat = [num for sublist in mat for num in sublist]    
#         n = len(flat_mat)
		
# 		# Check if reshape is invalid
#         if n%r:
#             return mat
        
#         k = n//r     # k is the number of elements per row 
#         return [ flat_mat[(i*k) : (i*k)+k] for i in range(r)]
    
# -------------------------------------------------------------------
#         flat_mat = []
#         for sublist in t:
#             for item in sublist:
#                 flat_mat.append(item)  
# -------------------------------------------------------------------
# Solution 1 - NumPy
# -------------------
        # try:
        #     return np.reshape(mat, (r, c)).tolist()
        # except:
        #     return mat
# -------------------------------------------------------------------
# Solution 2 - Oneliner
# ---------------------
        return mat if len(sum(mat, [])) != r * c else map(list, zip(*([iter(sum(mat, []))]*c)))

# A more readable version of that:
# -------------------------------    
    # flat = sum(mat, [])
    # if len(flat) != r * c:
    #     return mat
    # tuples = zip(*([iter(flat)] * c))
    # return map(list, tuples)

# -------------------------------------------------------------------


            
            