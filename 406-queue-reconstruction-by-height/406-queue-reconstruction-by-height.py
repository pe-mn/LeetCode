class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort the people from tall to short
        # insert from tall to short (insert at index = p[1])
        people.sort(key=lambda p: (-p[0], p[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res        
        
# Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
# For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
# E.g.
# input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# subarray after step 1: [[7,0], [7,1]]
# subarray after step 2: [[7,0], [6,1], [7,1]]
# ...

# It's not the most concise code, but I think it well explained the concept.


# EDIT:
# Please also check:
# @tlhuang 's concise Python code.
# @wsurvi 's 4 lines Python code.
# @tonygogogo 's 8 lines C++ solution.
# @zeller2 's Java version.
# @hotpro 's Java 8 solution.