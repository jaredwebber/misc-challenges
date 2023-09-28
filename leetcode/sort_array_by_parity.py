# https://leetcode.com/problems/sort-array-by-parity


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        nums.sort(key=lambda x: x % 2)
        return nums
