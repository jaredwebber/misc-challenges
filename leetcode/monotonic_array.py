# https://leetcode.com/problems/monotonic-array


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return True

        inc: int = 0
        last: int = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < last:
                if inc == -1:
                    return False
                inc = 1
            elif nums[i] > last:
                if inc == 1:
                    return False
                inc = -1
            last = nums[i]

        return True
