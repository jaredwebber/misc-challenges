# https://leetcode.com/problems/height-checker


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        ordered = sorted(heights)
        count: int = 0
        for i in range(len(heights)):
            if heights[i] != ordered[i]:
                count += 1
        return count
