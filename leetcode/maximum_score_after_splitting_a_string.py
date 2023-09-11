# https://leetcode.com/problems/maximum-score-after-splitting-a-string


class Solution:
    def maxScore(self, s: str) -> int:
        num_ones: int = 0
        for i in s:
            if i == "1":
                num_ones += 1

        left_count: int = 1 if s[0] == "0" else 0
        right_count: int = num_ones if s[0] != "1" else num_ones - 1
        max_score: int = left_count + right_count

        for i in range(1, len(s) - 1):
            if s[i] == "1":
                right_count -= 1
            if s[i] == "0":
                left_count += 1
            max_score = max(max_score, left_count + right_count)

        return max_score
