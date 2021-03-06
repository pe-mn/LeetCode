class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
        
# In case you need a code without using lib to count the bit:
# -----------------------------------------------------------
        # return sorted(arr, key = lambda num : (sum((num >> i) & 1 for i in range(32)), num))


#         def bit_count(x: int) -> int:
#             bit = 0
#             while x > 0:
#                 bit += x % 2
#                 x //= 2
#             return bit
        
#         return sorted(arr, key=lambda x: (bit_count(x), x))

# Comment regarding i -> Integer.bitCount(i) * 10000 + i to answer any potential question. It's essentially hashing the original numbers into another number generated from the count of bits and then sorting the newly generated numbers. so why 10000? simply because of the input range is 0 <= arr[i] <= 10^4.
# For instance [0,1,2,3,5,7], becomes something like this [0, 10001, 10002, 20003, 20005, 30007

# 0 has 0 number of bits  --> 0 * 10000 + 0 = 0
# 1,2 have 1 bit set      --> 1 * 10000 + 1 = 10001  &  1 * 10000 + 2 = 10002
# 3,5 have 2 bits set     --> 2 * 10000 + 3 = 20003  &  2 * 10000 + 5 = 20005
# 7 has 3 bits set        --> 3 * 10000 + 7 = 30007