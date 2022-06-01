class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# In case you need a code without using lib to count the bit:
# -----------------------------------------------------------
#         def bit_count(x: int) -> int:
#             bit = 0
#             while x > 0:
#                 bit += x % 2
#                 x //= 2
#             return bit
        
#         return sorted(arr, key=lambda x: (bit_count(x), x))

# Comment regarding i -> Integer.bitCount(i) * 10000 + i to answer any potential question. It's essentially hashing the original numbers into another number generated from the count of bits and then sorting the newly generated numbers. so why 10000? simply because of the input range is 0 <= arr[i] <= 10^4.
# For instance [0,1,2,3,5,7], becomes something like this [0, 10001, 10002, 20003, 20005, 30007