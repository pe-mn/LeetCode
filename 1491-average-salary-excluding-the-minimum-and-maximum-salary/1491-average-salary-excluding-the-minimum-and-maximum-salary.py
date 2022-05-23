# https://www.geeksforgeeks.org/remove-all-the-occurrences-of-an-element-from-a-list-in-python/

class Solution:
    def average(self, salary: List[int]) -> float:
        # salary_new = [ i for i in salary if i not in [min(salary),max(salary)] ]
        # return statistics.mean(salary_new)
    
#----------------------------------------------------------------------------------------

        salary_new = list(filter((min(salary)).__ne__, salary))
        salary_new = list(filter((max(salary)).__ne__, salary_new))
        return statistics.mean(salary_new)     
        