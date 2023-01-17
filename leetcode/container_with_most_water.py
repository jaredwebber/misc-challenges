# https://leetcode.com/problems/container-with-most-water/description/


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left: int = 0
        right: int = len(height) - 1
        most: int = 0

        while left < right:
            min_height = min(height[left], height[right])
            most = max(most, (right - left) * min_height)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return most
