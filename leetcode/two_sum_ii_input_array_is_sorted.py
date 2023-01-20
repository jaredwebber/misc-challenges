# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left: int = 0
        right: int = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

        return []
