class NumArray:
    def __init__(self, nums: List[int]):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums: 
            self.accu += self.accu[-1] + num,

    def sumRange(self, left: int, right: int) -> int:
        """
        sum of elements nums[left..right], inclusive.
        :type left: int 
        :type right: int
        :rtype: int 
        """
        return self.accu[right + 1] - self.accu[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)