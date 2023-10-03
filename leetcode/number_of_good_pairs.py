# https://leetcode.com/problems/number-of-good-pairs


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        pairs: int = 0
        num_count: dict[int, int] = {}
        for i in nums:
            if num_count.get(i):
                pairs += num_count.get(i)
            else:
                num_count[i] = 0
            num_count[i] += 1
        return pairs
