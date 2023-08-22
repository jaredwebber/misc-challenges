# https://leetcode.com/problems/majority-element


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter: dict[int, int] = {}
        for i in nums:
            if counter.get(i):
                if counter.get(i) + 1 > len(nums) / 2:
                    return i
                counter[i] += 1
            else:
                counter[i] = 1
        return nums[0]
