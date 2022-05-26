class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # Handle Edge Caces
        if all( (point[0]!=x and point[1]!=y) for point in points):
            return -1
                
        distance = float('inf')
        index = -1                
        for point in points:
            if point[0]==x:
                if abs(point[1]-y) < distance:
                    distance = abs(point[1]-y)
                    index = points.index(point)
            
            if point[1]==y:
                if abs(point[0]-x) < distance: 
                    distance = abs(point[0]-x)
                    index = points.index(point)                
             
        return index 

# ---------------------------------------------------------------------

#         validPoints = []
        
#         for index, point in enumerate(points):
#             if point[0] == x or point[1] == y:
#                 distance = abs(x - point[0]) + abs(y - point[1])
#                 validPoints.append((point[0], point[1], distance, index))
        
#         validPoints.sort(key = lambda x: (x[2], x[3]))
        
#         return -1 if not len(validPoints) else validPoints[0][3]

# ---------------------------------------------------------------------
    
# # index, distance | if valid    
#         valid_point = 
#         [
#             (i, abs(x - point[0]) + abs(y - point[1]))
#             for i, point in enumerate(points)
#             if any((x == point[0], y == point[1]))
#         ]

#         if not valid_point:
#             return -1
#         elif len(valid_point) > 1:
#             return sorted(valid_point, key=lambda x: (x[1], x[0]))[0][0]
#         else:
#             return valid_point[0][0]
        
# ---------------------------------------------------------------------

#         # This Finds the smallest distance, not the index!!!
#         distances = []
#         for point in points:
#             if point[0]==x:
#                 distances.append(abs(point[1]-y))
            
#             if point[1]==y:
#                 distances.append(abs(point[0]-x))
             
#         distances.sort()
#         return distances[0]

# ---------------------------------------------------------------------

# # Another way to loop
#         i = 0
#         for x1,y1 in points:
#             if x == x1 or y == y1:
#                 if(abs(x1 - x) + abs(y1 - y)< distance):
#                     distance = abs(x1 - x) + abs(y1 - y)
#                     index = i
#             i+=1