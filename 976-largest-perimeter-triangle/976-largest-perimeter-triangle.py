class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        '''
  Therefore, for a triangle with non-zero area, the following expression must hold
  true:
    0 < a <= b <= c
    a + b > c
  To be clear, the sum of the two shortest sides of the triangle must be greater than
  the longest side.

  Thus, we simply need to sort the list, so that we choose the largest possible a, b,
  and c that will form a civilized triangle.

  Complexity Analysis
  Time Complexity: O(n log n), where n is the length of nums.
  Space Complexity: O(1).
        '''
        # nums.sorted(reverse=True)
        nums = sorted(nums, reverse=True)
        for i in range(len(nums) - 2):
            a, b, c = nums[i+2], nums[i+1], nums[i]
            if a + b > c:
                return a + b + c
        return 0        