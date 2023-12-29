# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule


class Solution:
    def minDifficulty(self, job_difficulty: list[int], d: int) -> int:
        n = len(job_difficulty)
        if n < d:
            return -1

        dp = [[float("inf")] * n for _ in range(d)]
        dp[0][0] = job_difficulty[0]

        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1], job_difficulty[i])

        for k in range(1, d):
            for i in range(k, n):
                local_max = job_difficulty[i]
                dp[k][i] = dp[k - 1][i - 1] + local_max

                for j in range(i - 1, k - 2, -1):
                    local_max = max(local_max, job_difficulty[j])
                    dp[k][i] = min(dp[k][i], dp[k - 1][j - 1] + local_max)

        return dp[d - 1][n - 1]


"""
job_difficulty = [6,5,4,3,2,1]
d = 6

6   | 6   | 6  | 6  | 6  | 6
inf | 11  | 10 | 9  | 8  | 7
inf | inf | 15 | 13 | 11 | 9
"""
