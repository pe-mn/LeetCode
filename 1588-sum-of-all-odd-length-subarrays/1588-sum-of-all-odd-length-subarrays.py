# https://stackoverflow.com/questions/27974126/how-to-get-all-combinations-of-length-n-in-python
# https://stackoverflow.com/questions/67638743/how-to-slice-sublists-to-given-length

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subs = []
        for n in range(1, len(arr)+1, 2):
            for i in range(len(arr)+1-n):
                subs.append(arr[i:i+n])
        return sum(sum(s) for s in subs)
            