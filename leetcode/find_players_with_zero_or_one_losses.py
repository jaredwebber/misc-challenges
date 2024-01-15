# https://leetcode.com/problems/find-players-with-zero-or-one-losses


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        results: dict[int, int] = {}
        played: set[int] = set()
        for win, loss in matches:
            results[loss] = results.get(loss, 0) + 1
            played.add(win)
            played.add(loss)

        zero: list[int] = []
        one: list[int] = []
        count: int = 0
        for i in played:
            count = results.get(i, 0)
            if count == 0:
                zero.append(i)
            elif count == 1:
                one.append(i)

        zero.sort()
        one.sort()
        return [zero, one]
