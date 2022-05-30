# A suggestion: strings are immutable, so each time you add a char to a string it creates a new string.
# I believe it is more efficient to use a list to append, and then join at the end.

class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()  
# -----------------------------------------------------------------
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in s)
# -----------------------------------------------------------------    
        # return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in s)
# -----------------------------------------------------------------

# The ASCII codes for A-Z is 65-90 and those for a-z is that range plus 32.
# Edit: Stop using range(65,91) to avoid creating these on every iteration.

        # res = ""
        # for char in s:
        #     if ord(char) >= 65 and ord(char) <= 90:
        #         res += chr(ord(char)+32)
        #     else:
        #         res += char   
        # return res