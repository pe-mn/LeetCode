# https://stackoverflow.com/questions/25216328/compare-strings-allowing-one-character-difference

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
# DP Solution
# ------------
        # dp = {}
        # for w in sorted(words, key=len):
        #     dp[w] = max(dp.get(w[:i] + w[i+1:], 0) + 1 for i in range(len(w)))
        #     print(dp)
        # return max(dp.values())            

# w[:i] + w[i+1:] --> split the word at eeach possible i and remove the ith char
# then check if it does exist in the dictionary
# The get() method returns the value of the item with the specified key.
# dictionary.get(keyname, value)

# Explanation
# Sort the words by word's length. (also can apply bucket sort)
# For each word, loop on all possible previous word with 1 letter missing.
# If we have seen this previous word, update the longest chain for the current word.
# Finally return the longest word chain.


# Complexity
# Time O(NlogN) for sorting,
# Time O(NSS) for the for loop, where the second S refers to the string generation and S <= 16.
# Space O(NS)
      
    
        dp = {}
        res = 1
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1 :]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
                    res = max(res, dp[word])
        return res
    
    
# Why max --> dp[word] = max(dp[word], dp[prev] + 1)   
# Example: words = [ "a", "ba", "cb", "cba", "dcba" ]
# The above code will calculate the dp[ "cba" ] value, firstly by considering dp[ "ba" ] (which is 2), and then by considering dp[ "cb" ] (which is 1).
# Hence, it finally calculates the value dp[ "cba" ] = 2 (whereas the correct value should be 3)
 

