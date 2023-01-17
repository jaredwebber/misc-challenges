# https://leetcode.com/problems/longest-consecutive-sequence/description/


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        vals: dict[int] = {}

        for i in nums:
            vals[i] = True

        longest: int = 0
        for i in nums:
            curr_len: int = 1
            curr_val: int = i - 1

            while vals.get(curr_val):
                vals[curr_val] = None
                curr_val -= 1
                curr_len += 1

            curr_val = i + 1
            while vals.get(curr_val):
                vals[curr_val] = None
                curr_val += 1
                curr_len += 1

            longest = max(curr_len, longest)

        return longest
