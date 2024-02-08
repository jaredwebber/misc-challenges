# https://leetcode.com/problems/ant-on-the-boundary


class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        offset: int = 0
        count: int = 0

        for i in nums:
            offset += i
            if offset == 0:
                count += 1

        return count
