# https://leetcode.com/problems/contains-duplicate/description/


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen: set[int] = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False


class SolutionTwo:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen: dict[int, bool] = {}
        for i in nums:
            if seen.get(i):
                return True
            seen[i] = True
        return False
