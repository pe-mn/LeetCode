# https://stackoverflow.com/questions/25216328/compare-strings-allowing-one-character-difference

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
# DP Solution
# ------------
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i+1:], 0) + 1 for i in range(len(w)))
            # print(dp)
        return max(dp.values())            

# w[:i] + w[i+1:] --> split the word at eeach possible i and remove the ith char
# then check if it does exist in the dictionary

# Explanation
# Sort the words by word's length. (also can apply bucket sort)
# For each word, loop on all possible previous word with 1 letter missing.
# If we have seen this previous word, update the longest chain for the current word.
# Finally return the longest word chain.


# Complexity
# Time O(NlogN) for sorting,
# Time O(NSS) for the for loop, where the second S refers to the string generation and S <= 16.
# Space O(NS)
                
        