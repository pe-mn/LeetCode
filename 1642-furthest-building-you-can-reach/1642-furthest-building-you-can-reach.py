# https://docs.python.org/3/library/heapq.html

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
# Priority Queue
        heap = []
        for i in range(len(heights) - 1):
            d = heights[i + 1] - heights[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(heights) - 1    

# PreWord
# Greedy soluton may be wrong.
# LeetCode messed up the test cases again.

# Explanation
# Heap heap store k height difference that we need to use ladders.
# Each move, if the height difference d > 0,
# we push d into the priority queue pq.
# If the size of queue exceed ladders,
# it means we have to use bricks for one move.
# Then we pop out the smallest difference, and reduce bricks.
# If bricks < 0, we can't make this move, then we return current index i.
# If we can reach the last building, we return A.length - 1.

# Complexity
# Time O(NlogK)
# Space O(K)

            