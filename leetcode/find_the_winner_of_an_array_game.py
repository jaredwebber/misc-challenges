# https://leetcode.com/problems/find-the-winner-of-an-array-game


class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        length: int = len(arr)
        consecutive: int = 0
        last: int = arr[0]
        temp: int = 0

        while consecutive < min(k, length - 1):
            if arr[0] > arr[1]:
                temp = arr[1]
                del arr[1]
            else:
                temp = arr[0]
                del arr[0]

            arr.append(temp)

            if last == arr[0]:
                consecutive += 1
            else:
                consecutive = 1
                last = arr[0]

        return last
