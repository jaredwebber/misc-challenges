# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones


# Poorly worded question
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
