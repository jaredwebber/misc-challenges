# https://leetcode.com/problems/surrounded-regions/description/


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        # Do not return anything, modify board in-place instead.

        # Mark edge-adjacent 0s with E
        # check top and bottom rows for Os
        for c in range(len(board[0])):
            if board[0][c] == "O":
                self.can_escape(board, 0, c)
            if board[len(board) - 1][c] == "O":
                self.can_escape(board, len(board) - 1, c)

        # check left and right columns for Os
        for r in range(1, len(board)):
            if board[r][0] == "O":
                self.can_escape(board, r, 0)
            if board[r][len(board[0]) - 1] == "O":
                self.can_escape(board, r, len(board[0]) - 1)

        # replace all remaining Os with X
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # replace E with O
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "E":
                    board[r][c] = "O"

    def can_escape(self, board: list[list[str]], row: int, col: int) -> None:
        if (
            row >= 0
            and col >= 0
            and row < len(board)
            and col < len(board[0])
            and board[row][col] == "O"
        ):
            board[row][col] = "E"
            self.can_escape(board, row + 1, col)
            self.can_escape(board, row - 1, col)
            self.can_escape(board, row, col + 1)
            self.can_escape(board, row, col - 1)
