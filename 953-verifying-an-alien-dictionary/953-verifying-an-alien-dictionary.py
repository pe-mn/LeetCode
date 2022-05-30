class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if sorted(words, key=lambda word: [order.index(c) for c in word]) == words:
            return True                
        return False
    
# Instead of using index() which requires finding the index of a char, a better alternative consists in building a hash map to be used in the sorting, in order to retrieve the index directly.

        # order_dic = dict(zip(order, range(len(order))))
        # if sorted(words, key=lambda word: [order_dic[c] for c in word]) == words:
        #     return True                
        # return False