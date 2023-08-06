# https://leetcode.com/problems/longest-turbulent-subarray


class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        if len(arr) == 1:
            return 1
        if len(arr) == 2:
            return 1 if arr[0] == arr[1] else 2

        left: int = 0
        right: int = 1
        maximum: int = 1
        last: int = 0

        while right < len(arr):
            maximum = max(maximum, right - left)
            if right - left == 1:
                last = 1 if arr[right] < arr[right - 1] else 2
            if last == 1 and arr[right] < arr[right - 1]:
                last = 2
            elif last == 2 and arr[right] > arr[right - 1]:
                last = 1
            else:
                if arr[right] == arr[right - 1]:
                    left = right
                else:
                    left = right - 1
                    right -= 1
            right += 1
            maximum = max(maximum, right - left)

        return maximum
