# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits


class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort()  # ensures items are in correct order if same number of 1s

        ones_arr: list[list[int]] = []
        for i, n in enumerate(arr):
            str_n: str = bin(n)[2:]
            ones_arr.append([n, str_n.count("1")])

        ones_arr.sort(key=lambda x: x[1])

        out: list[int] = []
        for i, j in ones_arr:
            out.append(i)

        return out
