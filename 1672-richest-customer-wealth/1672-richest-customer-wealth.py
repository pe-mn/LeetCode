import numpy as np 

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # wealth = [sum(l) for l in accounts]
        # return max(wealth)
    
 # -----------------------------------------------------------------
   
        # return max(sum(acc) for acc in accounts)

# -----------------------------------------------------------------

        # return max(map(sum, accounts))

# -----------------------------------------------------------------
    
         # return max(np.sum(accounts,axis=1))

# -----------------------------------------------------------------

# Approach:
# For every person, add his wealth from all the banks ie. for every row, sum all the column values and store in totalWealth.
# If totalWealth is more than maxWealth, then update maxWealth.

	    maxWealth = 0
	    for i in range(len(accounts)):
	        totalWealth = sum(accounts[i])
	        maxWealth = max(maxWealth, totalWealth)
	    return maxWealth
        