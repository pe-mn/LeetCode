class Solution:
    def isHappy(self, n: int) -> bool:
#         sum = 0
#         counter = 0
#         for i in str(n):
#             sum += int(i)**2
#             if sum == 1:
#                 return True
         
#         counter += 1
#         sum = isHappy(sum)
        
#         if counter == 20:
#             return False

# ----------------------------------------------------

        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(x) **2 for x in str(n))
        return n == 1

# n = sum([int(x) **2 for x in str(n)]) will calculate the next number.

# You can reduce the memory usage a little bit by replacing n = sum([int(i) ** 2 for i in str(n)]) with n = sum(int(i) ** 2 for i in str(n)). Not a big deal in this case, but generator expressions are useful!

# ----------------------------------------------------

# Exit Condition 1: Number is Happy (n == 1)
# Exit Condition 2: Number endlessly loops without reaching 1 (n in n_hash)  

#         n_hash = set()
#         while True:
#             if n == 1:
#                 return True

#             if n in n_hash:
#                 return False
#             else:
#                 n_hash.add(n)
#                 n = sum(int(i)**2 for i in list(str(n)))

# ----------------------------------------------------

#     mem = set()
#     while n != 1:
#         n = sum(int(i) ** 2 for i in str(n))
#         if n in mem:
#             return False
#         else:
#             mem.add(n)
#     else:
#         return True
                
# ----------------------------------------------------

# https://leetcode.com/problems/happy-number/discuss/56918/All-you-need-to-know-about-testing-happy-number! 

# https://leetcode.com/problems/happy-number/discuss/56919/Explanation-of-why-those-posted-algorithms-are-mathematically-valid
    
# First of all, it is easy to argue that starting from a number I, if some value - say a - appears again during the process after k steps, the initial number I cannot be a happy number. Because a will continuously become a after every k steps.

# Therefore, as long as we can show that there is a loop after running the process continuously, the number is not a happy number.

