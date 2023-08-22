# https://leetcode.com/problems/can-place-flowers


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) < 3:
            return (flowerbed not in [[0, 1], [1, 0], [1]] and n != 2) or n == 0

        if len(flowerbed) == 3:
            return (n == 1 and flowerbed in [[0, 0, 1], [1, 0, 0]]) or (
                n <= 2 and flowerbed == [0, 0, 0]
            )

        for i in range(1, len(flowerbed) - 1):
            if (
                (i == len(flowerbed) - 2 or flowerbed[i - 1] == 0)
                and flowerbed[i] == 0
                and (i == 1 or flowerbed[i + 1] == 0)
            ):
                if i == 1 and flowerbed[i - 1] == 0:
                    flowerbed[i - 1] = 1
                else:
                    flowerbed[i] = 1
                n -= 1
        return n <= 0
