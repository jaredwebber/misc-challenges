# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        duplicates: int = 0
        index: int = 1
        current: int = nums[0]
        current_count: int = 1

        while index < len(nums):
            if nums[index] == current:
                if current_count < 2:
                    current_count += 1
                else:
                    nums[index] = 10001  # > max allowed value
                    duplicates += 1
            else:
                current = nums[index]
                current_count = 1
            index += 1

        nums.sort()

        return len(nums) - duplicates
