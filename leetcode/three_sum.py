# https://leetcode.com/problems/3sum


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        num_map: dict[int, int] = {}
        sums: list[int] = []

        for i in range(len(nums)):
            num_map[nums[i]] = i

        i_index: int = 0
        j_index: int = 0
        last_i: int = 100001
        last_j: int = 100001

        while i_index < len(nums):
            if nums[i_index] != last_i:
                j_index = i_index + 1
                last_j = 100001
                while j_index < len(nums):
                    if last_j != nums[j_index]:
                        if (
                            num_map.get(0 - nums[i_index] - nums[j_index])
                            and num_map.get(0 - nums[i_index] - nums[j_index]) > j_index
                        ):
                            sums.append([nums[i_index], nums[j_index], 0 - nums[i_index] - nums[j_index]])
                    last_j = nums[j_index]
                    j_index += 1
            last_i = nums[i_index]
            i_index += 1

        return sums
