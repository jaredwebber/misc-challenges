# https://leetcode.com/problems/valid-mountain-array


class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        if len(arr) < 3:
            return False

        if arr[0] >= arr[1]:
            return False

        increasing: bool = True
        last: int = -1
        for i in arr:
            if increasing and i > last or not increasing and i < last:
                pass
            elif increasing and i < last:
                increasing = False
            else:
                return False
            last = i
        return not increasing
