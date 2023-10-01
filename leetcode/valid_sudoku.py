# https://leetcode.com/problems/valid-sudoku


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        quadrant_map: dict[int, int] = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2}
        nine_by_nine_map: list[list[set[int]]] = [[set(), set(), set()], [set(), set(), set()], [set(), set(), set()]]
        col_map: list[set[int]] = [set() for _ in range(9)]

        for i in range(9):
            curr_row: set[int] = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if (
                    board[i][j] in nine_by_nine_map[quadrant_map[i]][quadrant_map[j]]
                    or board[i][j] in curr_row
                    or board[i][j] in col_map[j]
                ):
                    return False
                nine_by_nine_map[quadrant_map[i]][quadrant_map[j]].add(board[i][j])
                curr_row.add(board[i][j])
                col_map[j].add(board[i][j])

        return True
