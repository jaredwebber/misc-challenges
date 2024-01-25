# https://leetcode.com/problems/consecutive-characters


class Solution:
    def maxPower(self, s: str) -> int:
        last: str = ""
        curr_len: int = 0
        max_len: int = 0

        for i in s:
            if i != last:
                max_len = max(max_len, curr_len)
                curr_len = 0
                last = i
            curr_len += 1

        return max(max_len, curr_len)
