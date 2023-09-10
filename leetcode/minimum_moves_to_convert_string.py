# https://leetcode.com/problems/minimum-moves-to-convert-string


class Solution:
    def minimumMoves(self, s: str) -> int:
        moves: int = 0
        index: int = 0

        while index < len(s):
            if s[index] == "X":
                moves += 1
                index += 2
            index += 1

        return moves
