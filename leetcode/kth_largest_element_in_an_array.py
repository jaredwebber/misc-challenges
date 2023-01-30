# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

from queue import PriorityQueue


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        q: PriorityQueue = PriorityQueue()
        for i in nums:
            q.put((-i, i))
        for i in range(k - 1):
            q.get()
        return q.get()[1]
