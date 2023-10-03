# https://leetcode.com/problems/sudoku-solver


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows: list[set[int]] = [set() for _ in range(9)]
        cols: list[set[int]] = [set() for _ in range(9)]
        squares: list[set[int]] = [set() for _ in range(9)]
        solved: list[bool] = [False]  # using reference to act as global variable

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num: int = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[3 * (i // 3) + (j // 3)].add(num)

        def backtrack(row: int, col: int) -> None:
            if row == 9:
                solved[0] = True
                return

            next_row: int = (row + 1) if col == 8 else row
            next_col: int = (col + 1) % 9

            if board[row][col] != ".":
                backtrack(next_row, next_col)
            else:
                for i in range(1, 10):
                    if i not in rows[row] and i not in cols[col] and i not in squares[3 * (row // 3) + (col // 3)]:
                        rows[row].add(i)
                        cols[col].add(i)
                        squares[3 * (row // 3) + (col // 3)].add(i)
                        board[row][col] = str(i)

                        backtrack(next_row, next_col)
                        if not solved[0]:  # dont overwrite when solved
                            rows[row].remove(i)
                            cols[col].remove(i)
                            squares[3 * (row // 3) + (col // 3)].remove(i)
                            board[row][col] = "."

        backtrack(0, 0)
