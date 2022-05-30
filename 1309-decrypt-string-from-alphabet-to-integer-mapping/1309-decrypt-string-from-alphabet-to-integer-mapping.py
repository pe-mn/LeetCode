class Solution:
    def freqAlphabets(self, s: str) -> str:
        # return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))
    
# The 97th character represents 'a' so you can just add the number to 96 to get the alphabet. 
# 65 --> A, 90 --> Z
# 65+32 -> a, 90+32 -> z

# Start from letter z (two digit numbers) and work backwords to avoid any confusion or inteference with one digit numbers. After replacing all two digit (hashtag based) numbers, we know that the remaining numbers will be simple one digit replacements.
# Note that ord('a') is 97 which means that chr(97) is 'a'. This allows us to easily create a character based on its number in the alphabet. For example, 'a' is the first letter in the alphabet. It has an index of 1 and chr(96 + 1) is 'a'.

        for i in range(26,0,-1): s = s.replace(str(i)+'#'*(i>9),chr(96+i))
        return s
    
# It is #*(i>9)
# If i>9 is True, it evaluates to 1. Hence '#'*1 means a single character '#'
# If i>9 is False, it evaluates to 0. Hence no #.


        