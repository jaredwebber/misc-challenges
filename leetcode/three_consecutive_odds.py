# https://leetcode.com/problems/three-consecutive-odds


class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for index in range(len(arr) - 2):
            if arr[index] % 2 != 0 and arr[index + 1] % 2 != 0 and arr[index + 2] % 2 != 0:
                return True

        return False
