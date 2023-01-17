# https://leetcode.com/problems/word-search/description/


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    board[r][c] = "-"
                    if self.search(board, r, c, 1, word):
                        return True
                    board[r][c] = word[0]
        return False

    def search(
        self, board: list[list[str]], row: int, col: int, index: int, word: str
    ) -> bool:
        if index == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False

        temp: str = board[row][col]
        board[row][col] = "-"
        found: bool = False
        # search above
        if row > 0 and board[row - 1][col] == word[index]:
            found = self.search(board, row - 1, col, index + 1, word)
        # search right
        if not found and col < len(board[0]) - 1 and board[row][col + 1] == word[index]:
            found = self.search(board, row, col + 1, index + 1, word)
        # search below
        if not found and row < len(board) - 1 and board[row + 1][col] == word[index]:
            found = self.search(board, row + 1, col, index + 1, word)
        # search left
        if not found and col > 0 and board[row][col - 1] == word[index]:
            found = self.search(board, row, col - 1, index + 1, word)

        board[row][col] = temp
        return found
