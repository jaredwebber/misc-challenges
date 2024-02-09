# https://leetcode.com/problems/longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: dict[str, int] = {}
        longest: int = 0
        start: int = 0

        for index, char in enumerate(s):
            seen = last_seen.get(char)
            if seen is not None and seen >= start:
                longest = max(longest, index - start)
                start = seen + 1
            last_seen[char] = index

        return max(longest, len(s) - start)
