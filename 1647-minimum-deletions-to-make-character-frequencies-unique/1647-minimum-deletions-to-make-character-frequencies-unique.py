class Solution:
    def minDeletions(self, s: str) -> int:
# Python 3 Greedy
        cnt, res, used = collections.Counter(s), 0, set()
        for ch, freq in cnt.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res
    
# Greedy works since we can only delete characters (we cannot add or replace characters).

# So, count each character first. For each 26 characters, check if it's count is already used. If so, delete characters until you find unused count, or reach zero.