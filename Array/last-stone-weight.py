"""
Last Stone Weight (LeetCode 1046)

You are given an array of integers stones where stones[i] is the weight of the ith stone.

On each turn, we choose the heaviest two stones and smash them together. Suppose the
heaviest two stones have weights x and y with x <= y. The result of this smash is:
- If x == y, both stones are destroyed.
- If x != y, the stone of weight x is destroyed, and the stone of weight y has new
  weight y - x.

At the end of the game, there is at most one stone left. Return the weight of the
last remaining stone. If there are no stones left, return 0.
"""

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Use negated values so heapq (min-heap) acts as a max-heap
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0


if __name__ == "__main__":
    s = Solution()
    assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeight([1]) == 1
    assert s.lastStoneWeight([1, 1]) == 0
    print("All tests passed.")
