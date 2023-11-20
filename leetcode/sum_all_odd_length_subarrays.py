# https://leetcode.com/problems/sum-of-all-odd-length-subarrays


class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total: int = 0
        for i in range(len(arr)):
            total += self.sum_odd(arr, i, i, 0)
        return total

    def sum_odd(self, arr: list[int], left: int, right: int, total: int) -> int:
        if left >= 0 and right < len(arr):
            if left != right:
                total += arr[left]

            total += arr[right]
            total += self.sum_odd(arr, left - 1, right + 1, total)

            return total
        else:
            return 0
