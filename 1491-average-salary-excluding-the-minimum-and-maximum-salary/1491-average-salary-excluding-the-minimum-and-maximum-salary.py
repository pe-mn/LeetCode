# https://www.geeksforgeeks.org/remove-all-the-occurrences-of-an-element-from-a-list-in-python/

# import numpy as np

class Solution:
    def average(self, salary: List[int]) -> float:
        # salary_new = [ i for i in salary if i not in [min(salary),max(salary)] ]
        # return statistics.mean(salary_new)
    
#----------------------------------------------------------------------------------------

        # salary_new = list(filter((min(salary)).__ne__, salary))
        # salary_new = list(filter((max(salary)).__ne__, salary_new))
        # return statistics.mean(salary_new)     

#----------------------------------------------------------------------------------------

# Note: use sort after set as set don't keep order
        salary_new = list(set(salary))
        salary_new.sort()
        return statistics.mean(salary_new[1:-1])
    
#----------------------------------------------------------------------------------------
    
# # since array of unique integers 
#         salary.sort()
#         return statistics.mean(salary[1:-1])

#----------------------------------------------------------------------------------------

# # since array of unique integers 

#         return (sum(salary)-min(salary)-max(salary)) / (len(salary)-2)

# # take salary sum and subtract both the min and max values 
# # divide by the length of the array minus 2 (excluding min and max values) 
# # and convert to float