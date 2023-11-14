# https://leetcode.com/problems/sort-the-students-by-their-kth-score


class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        kth_scores: list[tuple[int, int]] = []
        for i in range(len(score)):
            kth_scores.append((score[i][k], score[i]))
        kth_scores.sort(key=lambda x: -x[0])

        for i in range(len(score)):
            score[i] = kth_scores[i][1]
        return score
