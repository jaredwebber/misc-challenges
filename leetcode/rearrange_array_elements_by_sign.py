# https://leetcode.com/problems/rearrange-array-elements-by-sign


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive: list[int] = []
        negative: list[int] = []
        for i in nums:
            if i > 0:
                positive.append(i)
            else:
                negative.append(i)

        result: list[int] = []

        while len(positive) > 0 and len(negative) > 0:
            result.append(positive.pop(0))
            result.append(negative.pop(0))

        if len(positive) > 0:
            result.append(positive.pop(0))

        return result
