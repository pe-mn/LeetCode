# sorted(iteraable, key, reverse=False)
# sorts the given sequence as well as set and dictionary(which is not a sequence)
# either in ascending order or in descending order
# This method doesn’t effect the original sequence.

# List_name.sort(key, reverse=False)
# unlike sorted it returns nothing 
# and makes changes to the original sequence
# Moreover, sort() is a method of list class and can only be used with lists.

# Lexicographical order in Python is the type of sorting in which the data elements appear in the dictionary order. In the lexicographical order data elements are sorted based on the alphabetical order.

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort(); prefix = ''; res = []
        for char in searchWord:
            prefix += char
            res.append([p for p in products if p.startswith(prefix)][:3])            
        return res

# --------------------------------------------------------------------------------------

        # products.sort()
        # res, prefix, i = [], '', 0
        # for c in searchWord:
        #     prefix += c
        #     i = bisect.bisect_left(products, prefix, i)
        #     res.append([w for w in products[i:i + 3] if w.startswith(prefix)])
        # return res
        
# Intuition
# In a sorted list of words,
# for any word A[i],
# all its sugested words must following this word in the list.

# For example, if A[i] is a prefix of A[j],
# A[i] must be the prefix of A[i + 1], A[i + 2], ..., A[j]

# Explanation
# With this observation,
# we can binary search the position of each prefix of search word,
# and check if the next 3 words is a valid suggestion.


# Complexity
# Time O(NlogN) for sorting
# Space O(logN) for quick sort.

# Time O(logN) for each query
# Space O(query) for each query
# where I take word operation as O(1)
            
            
        