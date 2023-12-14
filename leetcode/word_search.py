# https://leetcode.com/problems/word-search/description/


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if len(word) > len(board) * len(board[0]):
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if self.search(board, r, c, 1, word):
                        return True
        return False

    def search(self, board: list[list[str]], row: int, col: int, index: int, word: str) -> bool:
        if index == len(word):
            return True

        board[row][col] = "-"
        found: bool = False
        # search above
        if row > 0 and board[row - 1][col] == word[index]:
            found = self.search(board, row - 1, col, index + 1, word)

        if not found:
            # search right
            if col < len(board[0]) - 1 and board[row][col + 1] == word[index]:
                found = self.search(board, row, col + 1, index + 1, word)
            if not found:
                # search below
                if row < len(board) - 1 and board[row + 1][col] == word[index]:
                    found = self.search(board, row + 1, col, index + 1, word)
                # search left
                if not found and col > 0 and board[row][col - 1] == word[index]:
                    found = self.search(board, row, col - 1, index + 1, word)

        board[row][col] = word[index - 1]
        return found
