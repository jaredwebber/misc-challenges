# https://leetcode.com/problems/relative-ranks


class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        ranking: list[list[str]] = []

        for i in range(len(score)):
            ranking.append([score[i], i])

        ranking.sort(key=lambda x: x[0], reverse=True)

        results: list[str] = ["0" for _ in range(len(score))]
        for i in range(len(ranking)):
            results[ranking[i][1]] = (
                str(i + 1)
                if i > 2
                else "Gold Medal"
                if i == 0
                else "Silver Medal"
                if i == 1
                else "Bronze Medal"
            )

        return results
