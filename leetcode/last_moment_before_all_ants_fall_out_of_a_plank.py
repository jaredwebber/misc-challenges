# https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank


class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        if not right:
            return max(left, default=0)
        return max(max(left, default=0), n - min(right))
