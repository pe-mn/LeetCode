class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w = ''
        for c1, c2 in zip(word1, word2):
            w += c1+c2  
        
        n1, n2 = len(word1), len(word2)
        if n1 == n2:
            return w 
        elif n1 > n2:
            return w + word1[n2: n2+(n1-n2)]
        else:
            return w + word2[n1: n1+(n2-n1)]
            