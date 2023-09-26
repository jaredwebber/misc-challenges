# https://leetcode.com/problems/determine-the-winner-of-a-bowling-game


class Solution:
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        one: int = 0
        two: int = 0

        double_one: int = 0
        double_two: int = 0
        for i in range(len(player1)):
            one += player1[i] if double_one < 1 else 2 * player1[i]
            if player1[i] == 10:
                double_one = 2
            else:
                double_one -= 1

            two += player2[i] if double_two < 1 else 2 * player2[i]
            if player2[i] == 10:
                double_two = 2
            else:
                double_two -= 1

        return 0 if one == two else 1 if one > two else 2
