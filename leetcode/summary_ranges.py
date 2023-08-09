# https://leetcode.com/problems/summary-ranges


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []

        summary: list[str] = []
        index: int = 1
        start: int = nums[0]
        last: int = nums[0]
        while index < len(nums):
            if nums[index] > last + 1:
                if start == last:
                    summary.append(str(start))
                else:
                    summary.append(f"{start}->{last}")
                start = nums[index]
            last = nums[index]
            index += 1
        if start == last:
            summary.append(str(start))
        else:
            summary.append(f"{start}->{last}")

        return summary
