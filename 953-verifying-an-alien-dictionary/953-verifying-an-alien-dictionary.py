class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # return sorted(words, key=lambda word: [order.index(c) for c in word]) == words
    
# Instead of using index() which requires finding the index of a char, a better alternative consists in building a hash map to be used in the sorting, in order to retrieve the index directly.

        # order_dic = dict(zip(order, range(len(order))))
        # if sorted(words, key=lambda word: [order_dic[c] for c in word]) == words:
        #     return True                
        # return False
        
# ---------------------------------------------------------------------------

# Lee215        
# Explanation
# Build a transform mapping from order,
# Find all alien words with letters in normal order.

# For example, if we have order = "xyz..."
# We can map the word "xyz" to "abc" or "123"

# Then we check if all words are in sorted order.

# Complexity
# Time O(NS)
# Space O(1)

        # m = {c: i for i, c in enumerate(order)}
        # words = [[m[c] for c in w] for w in words]
        # return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))

# Minor bug in the python code: the < in this line should be <=
# return all(w1 < w2 for w1, w2 in zip(words, words[1:]))
# Note the test cases are missing examples with duplicate words, which is why this passes.
    
# Python 1-line
# Slow, just for fun   
# -------------------
        # return words == sorted(words, key=lambda w: list(map(order.index, w)))

# ---------------------------------------------------------------------------
# https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/203175/Python-straightforward-solution

        # ind = {c: i for i, c in enumerate(order)}
        # for a, b in zip(words, words[1:]):
        #     if len(a) > len(b) and a[:len(b)] == b:
        #         return False
        #     for s1, s2 in zip(a, b):
        #         if ind[s1] < ind[s2]:
        #             break
        #         elif ind[s1] > ind[s2]:
        #             return False
        # return True
    
# ---------------------------------------------------------------------------
# https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/361525/Python-Solution-with-Detailed-Explaination-for-Beginner

        dic = {}
        new_words = []
        for i, ch in enumerate(order):
            dic[ch] = i
        for w in words:
            new = []
            for c in w:
                new.append(dic[c])
            new_words.append(new)
        for w1, w2 in zip(new_words, new_words[1:]):
            if w1 > w2:
                return False
        return True