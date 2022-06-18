# https://leetcode.com/problems/prefix-and-suffix-search/discuss/1185171/Python-Two-solutions-%2B-Trie-and-bruteforce-explained

class WordFilter:
    def __init__(self, words: List[str]):        
        self.d = {}
        for i, word in enumerate(words):
            for p, s in product(range(len(word) + 1), repeat=2):
                self.d[word[:p], word[s:]] = i

    def f(self, prefix: str, suffix: str) -> int:
        return self.d.get((prefix, suffix), -1) 

# ----------------------------------------------------------------------
# https://leetcode.com/problems/prefix-and-suffix-search/discuss/483341/Short-Python
# Time Limit Exceeded
        # W = ' '.join(w + '=' + w for w in words[::-1])
        # self.f = lambda p, s: W.count('=', W.find(s + '=' + p)) - 1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)