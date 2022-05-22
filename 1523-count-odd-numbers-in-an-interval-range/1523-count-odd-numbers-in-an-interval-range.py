class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # count = 0
        # for i in range(low, high+1):
        #     if i%2 != 0:
        #         count+=1
        # return count
    
#------------------------------------------------------------------------------------- 

        diff = high - low
        if low%2 == 0 and high%2 == 0:
            return diff // 2
        else:
            return diff // 2 + 1
        return diff // 2
            
#-------------------------------------------------------------------------------------    

        # # low%2 --> odd number
        # diff = high - low
        # return diff//2 + 1 if low%2 or high%2 else diff//2        