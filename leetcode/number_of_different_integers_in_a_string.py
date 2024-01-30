# https://leetcode.com/problems/number-of-different-integers-in-a-string/


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        integers: set[int] = set()
        curr: str = ""

        for i in word:
            if i.isnumeric():
                curr += i
            elif len(curr) > 0:
                integers.add(int(curr))
                curr = ""

        if len(curr) > 0:
            integers.add(int(curr))

        return len(integers)
