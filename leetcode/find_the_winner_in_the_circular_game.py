# https://leetcode.com/problems/find-the-winner-of-the-circular-game


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends: list[int] = []
        for i in range(1, n + 1):
            friends.append(i)

        index: int = 0
        while len(friends) > 1:
            index = (index + k - 1) % len(friends)
            friends.pop(index)

        return friends[0]
