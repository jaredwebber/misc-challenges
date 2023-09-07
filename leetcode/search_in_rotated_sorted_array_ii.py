# https://leetcode.com/problems/search-in-rotated-sorted-array-ii


# as the values in nums are no longer guarenteed to be unique, the runtime of binary search
# can be close to O(n) average case, making a linear search a simple, near-equivalent option
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        return target in nums
