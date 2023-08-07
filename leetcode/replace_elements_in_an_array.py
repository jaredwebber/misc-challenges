# https://leetcode.com/problems/replace-elements-in-an-array


class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        num_map: dict(int, int) = {}
        for i in range(len(nums)):
            num_map[nums[i]] = i

        index: int
        for o in operations:
            index = num_map.pop(o[0])
            nums[index] = o[1]
            num_map[o[1]] = index

        return nums
