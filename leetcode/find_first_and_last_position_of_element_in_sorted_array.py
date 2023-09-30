# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start_end: list[int] = [-1, -1]

        if len(nums) < 1:
            return start_end

        low: int = 0
        mid: int = 0
        hi: int = len(nums) - 1

        # binary search for first index
        if nums[0] == target:
            start_end[0] = 0
        else:
            while low <= hi:
                mid = (low + hi) // 2
                if nums[mid] == target:
                    if nums[mid - 1] == target:
                        hi = mid - 1
                    else:
                        start_end[0] = mid
                        break
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    low = mid + 1

        # binary search for last index
        if nums[len(nums) - 1] == target:
            start_end[1] = len(nums) - 1
        elif start_end[0] == len(nums) - 1 or nums[start_end[0] + 1] != target:
            return [start_end[0], start_end[0]]
        else:
            low = max(0, low + 1)
            hi = len(nums) - 1
            while low <= hi:
                mid = (low + hi) // 2
                if nums[mid] == target:
                    if nums[mid + 1] == target:
                        low = mid + 1
                    else:
                        start_end[1] = mid
                        break
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    low = mid + 1

        return start_end
