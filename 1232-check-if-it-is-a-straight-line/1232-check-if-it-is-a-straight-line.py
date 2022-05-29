# ZeroDivisionError: division by zero
# [[0,0],[0,1],[0,-1]]

class Solution:   
    # def slope(self, l1, l2):
    #     if l2[0] == l1[0]:
    #         return 10000        
    #     return (l2[1]-l1[1])/(l2[0]-l1[0]) 
            
    # def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    #     s = self.slope(coordinates[0], coordinates[1])        
    #     if all(self.slope(coordinates[0], coordinates[i]) == s for i in range(2, len(coordinates))):
    #         return True     
    #     return False
    
# https://stackoverflow.com/questions/3813681/checking-to-see-if-3-points-are-on-the-same-line
# You can check if the area of the ABC triangle is 0:

# --------------------------------------------------------------------------

# In order to avoid being divided by 0, use multiplication form:
# ---------------------------------------------------------------
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True
 

    # def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    #     (x0, y0), (x1, y1) = coordinates[: 2]
    #     return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)
    

    
    


        