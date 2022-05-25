class Solution:
    def subtractProductAndSum(self, n: int) -> int:        
        product = 1
        summation = 0
        for i in str(n):
            product = product * int(i)
            summation = summation + int(i)
        
        return (product - summation)    
    
# -----------------------------------------------------------------   

		# # l = map(int, str(n))
		# l=[int(i) for i in str(n)]
		# return math.prod(l)-sum(l)    
 
# -----------------------------------------------------------------   

## Best Approach
# # if the number can be divided by 10, the the product is 0
# # if not, then the remaining (n%10) is the first digit
# # n//10 --> gives the remaining digits
#         prod=1
#         Sum=0
#         while n>0:
#             a=n%10
#             prod*=a
#             Sum+=a
#             n=n//10
#         return prod-Sum