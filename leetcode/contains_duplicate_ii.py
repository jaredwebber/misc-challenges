# https://leetcode.com/problems/contains-duplicate-ii


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        range_dict: dict[int] = {}
        left: int = 0
        right: int = 0

        while right < len(nums) and right <= k:
            if range_dict.get(nums[right]):
                return True
            range_dict[nums[right]] = 1
            right += 1

        while right < len(nums):
            range_dict[nums[left]] = None
            left += 1

            if range_dict.get(nums[right]):
                return True

            range_dict[nums[right]] = 1
            right += 1

        return False
