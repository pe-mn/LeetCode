class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # res = [0]
        # for i, word in enumerate(words):
        #     for j in range(i+1, len(words)):
        #         if all(char not in word for char in words[j]):
        #             res.append(len(word)*len(words[j]))
        # return max(res)
    
# ------------------------------------------------------------------

        res = [0]
        for i, word in enumerate(words):
            for j in range(i+1, len(words)):
                check = True
                for char in word:
                    if char in words[j]:
                        check = False
                        break
                if check:
                    res.append(len(word)*len(words[j]))
        return max(res)