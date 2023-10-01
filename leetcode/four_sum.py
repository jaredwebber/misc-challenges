# https://leetcode.com/problems/4sum/submissions/


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        return self.k_sum(4, nums, 0, target, [], [])

    def k_sum(self, k: int, nums: list[int], start: int, target: int, curr: list[int], sums: list[list[int]]) -> None:
        if k == 2:  # base case
            left: int = start
            right: int = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    sums.append(curr + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        else:  # recurse
            for i in range(start, len(nums) - k + 1):
                if i == start or nums[i] != nums[i - 1]:
                    curr.append(nums[i])
                    self.k_sum(k - 1, nums, i + 1, target - nums[i], curr, sums)
                    curr.pop()

        return sums
