class Solution:
    def isValid(self, s: str) -> bool:
        
# [Python] is this a cheating method? accepted with 40ms, easy to understand, but
#         if len(s) % 2 != 0:
#             return False
            
#         while '()' in s or '{}' in s or '[]' in s:
#             s = s.replace('{}','').replace('()','').replace('[]','')
        
#         return s == ''

# --------------------------------------------------------------------------

        # d = {'(':')', '{':'}','[':']'}
        # stack = []
        # for i in s:
        #     if i in d:  # 1
        #         stack.append(i)
        #     elif len(stack) == 0 or d[stack.pop()] != i:  # 2
        #         return False
        # return len(stack) == 0 # 3
	
# 1. if it's the left bracket then we append it to the stack
# 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 3. finally check if the stack still contains unmatched left bracket

# --------------------------------------------------------------------------

        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

        