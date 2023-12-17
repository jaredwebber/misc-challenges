# https://leetcode.com/problems/battleships-in-a-board


class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        count: int = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    count += 1
                    self.fill(board, i, j)

        return count

    def fill(self, board: list[list[int]], row: int, col: int) -> None:
        board[row][col] = "."
        if row - 1 >= 0 and board[row - 1][col] == "X":
            self.fill(board, row - 1, col)
        if row + 1 < len(board) and board[row + 1][col] == "X":
            self.fill(board, row + 1, col)
        if col - 1 >= 0 and board[row][col - 1] == "X":
            self.fill(board, row, col - 1)
        if col + 1 < len(board[0]) and board[row][col + 1] == "X":
            self.fill(board, row, col + 1)
