class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
# we can reverse the problem and 
# get the minimum sum of a continuous sub array 
        size = len(cardPoints) - k   # The size of the subArray 
        # The sum from the 1st element to the size of the subArray 
        minSubArraySum = curr = sum(cardPoints[:size]) 
        
        for i in range(len(cardPoints) - size):
            # Subtract the an element from the beginning of the subArray 
            # And Add another element at the end
            curr += cardPoints[size + i] - cardPoints[i]
            minSubArraySum = min(minSubArraySum, curr)
            
        return sum(cardPoints) - minSubArraySum        