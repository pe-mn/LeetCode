import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat_mat = [num for sublist in mat for num in sublist]
        
        n = len(flat_mat)
        if n%r:
            return mat
        
        k = n//r
        reshaped = []
        for i in range(r):
            reshaped.append(flat_mat[(i*k) : (i*k)+k])
            
        return reshaped
    
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

# -------------------------------------------------------------------

# -------------------------------------------------------------------


            
            