import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:        
#         product = 1
#         summation = 0
#         for i in str(n):
#             product = product * int(i)
#             summation = summation + int(i)
        
#         return (product - summation)    
    
# -----------------------------------------------------------------   

        # # l = map(int, str(n))
        # l = [int(i) for i in str(n)]
        # return math.prod(l)-sum(l)    
 
# -----------------------------------------------------------------   

# Best Approach
# if the number can be divided by 10, the the product is 0
# if not, then the remaining (n%10) is the first digit
# n//10 --> gives the remaining digits
   
			# s, p = 0, 1
			# while n:
			# # Find the trailing digit
			# num = n % 10
			# s = s + num
			# p = p * num
			# # Update n by removing the last digit
			# n = n // 10
			# return p - s
    
# -----------------------------------------------------------------   
    
        digits = [int(x) for x in str(n)]
        return reduce(lambda x, y: x * y, digits) - sum(digits)