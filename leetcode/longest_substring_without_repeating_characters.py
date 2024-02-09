# https://leetcode.com/problems/longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: dict[str, int] = {}
        longest: int = 0
        start: int = 0

        for index, char in enumerate(s):
            if last_seen.get(char) is not None and last_seen.get(char) >= start:
                longest = max(longest, index - start)
                start = last_seen.get(char) + 1
            last_seen[char] = index

        return max(longest, len(s) - start)
