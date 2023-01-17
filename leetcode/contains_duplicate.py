# https://leetcode.com/problems/contains-duplicate/description/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        bruh: set[int] = set()
        for i in nums:
            if i in bruh:
                return True
            bruh.add(i)
        return False
