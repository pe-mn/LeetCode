class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # res = [0]
        # for i, word in enumerate(words):
        #     for j in range(i+1, len(words)):
        #         if all(char not in set(words[j]) for char in set(word)):
        #             res.append(len(word)*len(words[j]))
        # return max(res)
    
# ------------------------------------------------------------------

        # res = [0]
        # for i, word in enumerate(words):
        #     for j in range(i+1, len(words)):
        #         check = True
        #         for char in set(word):
        #             if char in set(words[j]):
        #                 check = False
        #                 break
        #         if check:
        #             res.append(len(word)*len(words[j]))
        # return max(res)
        
# ------------------------------------------------------------------

# faster than 91.46% of Python3 online submissions
# -------------------------------------------------
        # d = {}
        # for w in words:
        #     mask = 0
        #     for c in set(w):
        #         mask |= (1 << (ord(c) - 97))
        #     d[mask] = max(d.get(mask, 0), len(w))
        # return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
    
# It would be better if you replace 97 with ord('a') to avoid magic numbers.

        # d = {}
        # for w in words:
        #     mask = reduce(operator.or_, (1 << (ord(c)-97) for c in set(w)), 0)
        #     d[mask] = max(d.get(mask, 0), len(w))
        # return max([d[a]*d[b] for a in d for b in d if not (a & b) ] or [0])
        
# [Python] Bitmask solution, explained
# -------------------------------------------------
# https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/1233802/Python-Bitmask-solution-explained

        d, ans = defaultdict(int), 0
        for word in words:
            for l in word:
                d[word] |= 1<<(ord(l) - 97)
                
        for w1, w2 in combinations(d.keys(), 2):
            if d[w1] & d[w2] == 0: 
                ans = max(ans, len(w1)*len(w2))
                
        return ans
