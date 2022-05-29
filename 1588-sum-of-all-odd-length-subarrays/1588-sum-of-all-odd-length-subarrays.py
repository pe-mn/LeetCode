# https://stackoverflow.com/questions/27974126/how-to-get-all-combinations-of-length-n-in-python
# https://stackoverflow.com/questions/67638743/how-to-slice-sublists-to-given-length

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
    #     subs = []
    #     for n in range(1, len(arr)+1, 2):
    #         for i in range(len(arr)+1-n):
    #             subs.append(arr[i:i+n])
    #     return sum(sum(s) for s in subs)
    
    
        # res = 0
        # for n in range(1, len(arr)+1, 2):
        #     for i in range(len(arr)+1-n):
        #         res += sum(arr[i:i+n])
        # return res
    
# Solution 1: Brute Force
# ------------------------
# Enumerate all possible odd length of subarray.
# Time O(n^3)
# Space O(1)

        # n = len(arr)
        # res = 0
        # for l in range(1, n + 1, 2):
        #     for i in range(n - l + 1):
        #         res += sum(arr[i:i + l])
        # return res
    
# Python 1 line
# --------------
        # return sum(sum(arr[i:i + l]) for l in range(1, len(arr)+1, 2) for i in range(len(arr)-l+1))

# -----------------------------------------------------------------------------------------------

        # res, n = 0, len(arr)
        # for i, a in enumerate(arr):
        #     res += ((i + 1) * (n - i) + 1) // 2 * a
        # return res

# Python 1 line
# --------------
        return sum(((i + 1) * (len(arr)-i) + 1) // 2 * a for i, a in enumerate(arr))
            