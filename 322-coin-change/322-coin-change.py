# -> int just tells that f() returns an integer (but it doesn't force the function to return an integer). It is called a return annotation, and can be accessed as f.__annotations__['return']
# coins: List[int], amount: int are parameter annotations

# -> int just tells that f() returns an integer (but it doesn't force the function to return an integer). It is called a return annotation, and can be accessed as f.__annotations__['return']
# coins: List[int], amount: int are parameter annotations

# Bottom Up DP(Tabulation)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        dp=[math.inf] * (amount+1)
        dp[0]=0
        
        for coin in coins:
            for i in range(coin, amount+1):
                if i-coin>=0:
                    dp[i]=min(dp[i], dp[i-coin]+1)
        
        return -1 if dp[-1]==math.inf else dp[-1]
#-----------------------------------------------------------------------------------

# Top Down DP(Memoization)
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:            
#         def coinChangeInner(rem, cache):
#             if rem < 0:
#                 return math.inf
#             if rem == 0:                    
#                 return 0       
#             if rem in cache:
#                 return cache[rem]
            
#             cache[rem] = min(coinChangeInner(rem-x, cache) + 1 for x in coins)                         
#             return cache[rem]      
        
#         ans = coinChangeInner(amount, {})
#         return -1 if ans == math.inf else ans 

#-----------------------------------------------------------------------------------

# class Solution:
#     @staticmethod # no self passed
#     def coinChange(coins, amount) -> int:
#         # 0: Sort Coins in Descending order
#         coins.sort(reverse=True)
        
#         # First: Handle edge case, where amount is less than any coins
#         if amount == 0:
#             return 0
#         if amount < min(coins):
#             return -1  
                    
#         # Second: check if amount is multiple of coins + any coins in the list 
#         if amount%coins[0] in coins:
#             return (amount//coins[0])+1        
        
#         i = 0
#         remaining = amount
#         for c in coins:          
#             if remaining < min(coins): 
#                 break   
            
#             # Third: check if amount is multiple of any coins 
#             if amount%c == 0 and amount/c <= i+1:
#                 return int(amount/c)
            
#             # More Work on Remaining
#             if remaining%c == 0:
#                 return int(remaining/c)+i  
                
#             if remaining%c in coins:
#                 return (remaining//c)+i+1 
                
#             if remaining%c not in coins:
#                 # Problem is possibly here!!
#                 i = i+int(remaining//c) 
#                 remaining = remaining%c                        
        
#         # Last: check if amount is multiple of any coins before returning -1
#         for c in coins: 
#             if amount%c == 0:
#                 return int(amount/c)              
        

#         return -1