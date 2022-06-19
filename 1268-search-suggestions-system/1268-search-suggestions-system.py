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
        products.sort()
        prefix = ''
        res = []
        for char in searchWord:
            prefix += char
            res.append([p for p in products if p.startswith(prefix)][:3])            
        return res
            
            
        