# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated


class Solution:
    def check(self, nums: list[int]) -> bool:
        min_pre_flip: int = nums[0]
        flipped_at: int = -1
        last: int = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < last:
                if flipped_at != -1:
                    return False
                flipped_at = last
            if flipped_at != -1 and (nums[i] > flipped_at or nums[i] > min_pre_flip):
                return False
            last = nums[i]

        return True
